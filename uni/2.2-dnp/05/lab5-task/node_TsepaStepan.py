from argparse import ArgumentParser
from bisect import bisect_left
from threading import Thread
from xmlrpc.client import ServerProxy
from xmlrpc.server import SimpleXMLRPCServer

M = 5
PORT = 1234
RING = [2, 7, 11, 17, 22, 27]


def build_url(node_id: int):
    return f"http://node_{node_id}:{PORT}"


class Node:
    def __init__(self, id_: int):
        self.id = id_
        self.successor_id = node_id
        self.data_dict = {}
        self.finger_table = []

        for i in range(M):
            self.finger_table.append(
                (node_id + 2 ** i) % (2 ** M)
            )

    def closest_preceding_node(self, id_: int):
        """Returns node_id of the closest preceeding node (from n.finger_table) for a given id"""
        for i in range(M - 1, -1, -1):
            if self.id < self.finger_table[i] < id_:
                return self.finger_table[i]

        return self.id

    def find_successor(self, id_: int):
        """Recursive function returning the identifier of the node responsible for a given id"""
        if id_ == self.id:
            return id_

        right_border = self.successor_id
        if self.successor_id < self.id:
            right_border += 2 ** M

        if self.id < id_ <= right_border:
            return self.successor_id
        else:
            cpn = self.closest_preceding_node(id_)
            return ServerProxy(build_url(cpn)) \
                .find_successor(id_)

    def put(self, key, value):
        """Stores the given key-value pair in the node responsible for it"""
        print(f"PUT: node_{self.id} {key}: {value}")
        if self.id == self.find_successor(key):
            return self.store_item(key, value)
        else:
            successor_url = build_url(self.find_successor(key))
            successor_node = ServerProxy(successor_url)

            return successor_node.put(key, value)

    def get(self, key):
        """Gets the value for a given key from the node responsible for it"""
        print(f"GET: node_{self.id} {key}")
        if self.id == self.find_successor(key):
            return self.retrieve_item(key)
        else:
            successor_url = build_url(self.find_successor(key))
            successor_node = ServerProxy(successor_url)
            return successor_node.get(key)

    def store_item(self, key, value):
        """Stores a key-value pair into the data store of this node"""
        self.data_dict[key] = value
        return True

    def retrieve_item(self, key):
        """Retrieves a value for a given key from the data store of this node"""
        if key in self.data_dict.keys():
            return self.data_dict[key]
        return None


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('node_id', type=int)

    node_id = parser.parse_args().node_id
    server = SimpleXMLRPCServer((f'node_{node_id}', PORT), allow_none=True)

    node_obj = Node(node_id)
    server.register_instance(node_obj)

    server.serve_forever()
