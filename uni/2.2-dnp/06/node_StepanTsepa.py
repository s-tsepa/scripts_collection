import random
import sched
import socket
import time
from threading import Thread
from argparse import ArgumentParser
from enum import Enum
from xmlrpc.client import ServerProxy
from xmlrpc.server import SimpleXMLRPCServer

PORT = 1234
CLUSTER = [1, 2, 3]
ELECTION_TIMEOUT = lambda: random.uniform(6, 8)
HEARTBEAT_INTERVAL = 5


class NodeState(Enum):
    """Enumerates the three possible node states (follower, candidate, or leader)"""
    FOLLOWER = 1
    CANDIDATE = 2
    LEADER = 3


def build_url(node_id: int):
    return f"http://node_{node_id}:{PORT}"


class Node:
    def __init__(self, node_id):
        """Non-blocking procedure to initialize all node parameters and start the first election timer"""
        self.node_id = node_id
        self.state = NodeState.FOLLOWER
        self.term = 0
        self.votes = {}
        self.log = []
        self.pending_entry = ''
        self.sched = sched.scheduler()
        self.election_timer = None
        self.heartbeat_timer = None

        # Start election timer for this node
        self.start_election_timer()

        print(f"Node started! State: {self.state}. Term: {self.term}")

    def is_leader(self):
        """Returns True if this node is the elected cluster leader and False otherwise"""

        return self.state == NodeState.LEADER

    def cancel_election_timer(self):
        if self.election_timer:
            self.sched.cancel(self.election_timer)
            self.election_timer = None

    def start_election_timer(self):
        """Starts election timer for this node"""
        timeout = ELECTION_TIMEOUT()
        print(f"Starting election timer for {timeout:.2f} seconds")
        self.election_timer = self.sched.enter(timeout, 1, self.hold_election)

    def reset_election_timer(self):
        """Resets election timer for this (follower or candidate) node and returns it to the follower state"""

        self.cancel_election_timer()
        self.start_election_timer()
        self.state = NodeState.FOLLOWER

    def hold_election(self):
        """Called when this follower node is done waiting for a message from a leader (election timeout)
            The node increments term number, becomes a candidate and votes for itself.
            Then call request_vote over RPC for all other online nodes and collects their votes.
            If the node gets the majority of votes, it becomes a leader and starts the hearbeat timer
            If the node loses the election, it returns to the follower state and resets election timer.
        """
        print(f"-------------------------------- Hold election --------------")

        self.term += 1
        self.state = NodeState.CANDIDATE
        self.votes = {self.node_id: True}
        self.start_election_timer()

        vote_count = 1  # Vote for self
        online_count = len(CLUSTER)

        for node_id in CLUSTER:
            if node_id != self.node_id:
                try:
                    url = build_url(node_id)
                    print(f"Requesting vote from {url}")

                    proxy = ServerProxy(url)
                    vote_granted = proxy.request_vote(self.term, self.node_id)
                    print(f"vote_granted from {node_id}: {vote_granted}")
                    if vote_granted:
                        vote_count += 1
                        self.votes[node_id] = True
                    else:
                        self.votes[node_id] = False
                except (socket.error or socket.timeout) as e:
                    print(e)
                    print(f"Node {node_id} is offline")
                    online_count -= 1
                    self.votes[node_id] = False

        if vote_count > online_count // 2:
            self.state = NodeState.LEADER
            print(f"================================  Node {self.node_id} is the new leader (term {self.term})")

            self.cancel_election_timer()
            self.append_entries()
        else:
            print(f"Lost the election with votes: {vote_count} (term {self.term})")
            self.votes = {}
            self.reset_election_timer()

    def request_vote(self, term, candidate_id):
        """Called remotely when a node requests voting from other nodes.
            Updates the term number if the received one is greater than `self.term`
            A node rejects the vote request if it's a leader or it already voted in this term.
            Returns True and update `self.votes` if the vote is granted to the requester candidate and False otherwise.
        """
        print(f"Got a vote request from {candidate_id} (term={term})")

        if term > self.term:
            self.term = term
            self.state = NodeState.FOLLOWER

        if self.is_leader() or candidate_id in self.votes:
            return False

        self.votes[candidate_id] = True
        self.reset_election_timer()
        return True

    def append_entries(self):
        """Called by leader every HEARTBEAT_INTERVAL, sends a heartbeat message over RPC to all online followers.
            Accumulates ACKs from followers for a pending log entry (if any)
            If the majority of followers ACKed the entry, the entry is committed to the log and is no longer pending
        """
        print("Sending a heartbeat to followers")

        count_acked = 1
        count_online = len(CLUSTER)

        for node_id in CLUSTER:
            if node_id != self.node_id:
                try:
                    print(f"Sending AppendEntries to {node_id}")
                    url = build_url(node_id)
                    proxy = ServerProxy(url)
                    ans = proxy.heartbeat(self.pending_entry)
                    count_acked += int(ans)
                except (socket.error or socket.timeout) as e:
                    # except Exception as e:
                    print(e)
                    print(f"Node {node_id} is offline")
                    count_online -= 1

        self.heartbeat_timer = self.sched.enter(HEARTBEAT_INTERVAL, 1, self.append_entries)

        if count_acked > count_online // 2:
            if self.pending_entry:
                self.log.append(self.pending_entry)
                self.pending_entry = ''
            return True
        return False

    def heartbeat(self, leader_entry):
        """Called remotely from the leader to inform followers that it's alive and supply any pending log entry
            Followers would commit an entry if it was pending before, but is no longer now.
            Returns True to ACK the heartbeat and False on any problems.
        """
        print(f"Heartbeat received from leader (entry='{leader_entry}')")

        if leader_entry:
            self.log.append(leader_entry)
        self.reset_election_timer()
        return True

    def leader_receive_log(self, log):
        """Called remotely from the client. Executed only by the leader upon receiving a new log entry
            Returns True after the entry is committed to the leader log and False on any problems
        """
        print(f"Leader received log '{log}' from client")

        init_len = len(self.log)
        self.pending_entry = log

        # Wait until next call of scheduled append_entries finishes, committing pending_entry to other nodes
        while True:
            time.sleep(0.1)
            if len(self.log) - init_len > 0:
                return True


if __name__ == '__main__':
    # TODO: Parse one integer argument (node_id), then create the node with that ID.
    # TODO: Start RPC server on 0.0.0.0:PORT and expose the node instance
    # TODO: Run the node scheduler in an isolated thread.
    # TODO: Handle KeyboardInterrupt and terminate gracefully.

    socket.setdefaulttimeout(0.5)

    parser = ArgumentParser()
    parser.add_argument('node_id', type=int)
    args = parser.parse_args()

    node_id = args.node_id
    node = Node(node_id)

    try:
        server = SimpleXMLRPCServer((f'node_{node_id}', PORT))
        server.register_instance(node)
        print(f"Listen: {server.server_address}")

        # Run the node scheduler in an isolated thread
        node_thread = Thread(target=node.sched.run, args=(), name=f"Thread sched: {node_id}")
        node_thread.daemon = True
        node_thread.start()

        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopping...")
