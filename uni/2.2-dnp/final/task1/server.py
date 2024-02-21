from dataclasses import dataclass
import socket
import json

SERVER_ADDR = ("0.0.0.0", 50000)
RECV_SIZE = 1024

@dataclass
class RR:
    type: str
    key: str
    value: str

RECORDS_LIST = [
    RR("A", "example.com", "1.2.3.4"),
    RR("PTR", "1.2.3.4", "example.com"),
]

def on_recv(sock, data, addr):
    d: dict = json.loads(data)
    type_str = d.get("type", None)
    key_str = d.get("key", None)

    matching_record = None

    for record in RECORDS_LIST:
        if record.type == type_str and record.key == key_str:
            matching_record = record
            break

    if type_str and key_str and matching_record:
        print(f"Found matching record: {matching_record}")
        to_send = json.dumps(matching_record.__dict__)

    else:
        print(f"Not found")
        d_to_send = d.copy()
        d_to_send["value"] = "NXDOMAIN"
        to_send = json.dumps(d_to_send)

    sock.sendto(to_send.encode("utf-8"), addr)

if __name__ == "__main__":

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(SERVER_ADDR)

    print(f"Server is listening on: {SERVER_ADDR}")

    try:
        while True:
            data, addr = server_socket.recvfrom(RECV_SIZE)
            data = data.decode("utf-8")
            on_recv(server_socket, data, addr)
    except KeyboardInterrupt:
        exit()
