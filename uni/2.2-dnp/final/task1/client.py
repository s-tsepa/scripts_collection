from dataclasses import dataclass
import socket
import json

SERVER_ADDR = ("127.0.0.1", 50000)

@dataclass
class Query:
    type: str
    key: str


if __name__ == "__main__":
    q1 = Query("A", "example.com")
    q2 = Query("PTR", "1.2.3.4")
    q3 = Query("CNAME", "moodle.com")

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:

        for qi in q1, q2, q3:
            to_send = json.dumps(qi.__dict__)

            print(f"Sending DNS query: {qi}")

            s.sendto(to_send.encode("utf-8"), SERVER_ADDR)

            data, addr = s.recvfrom(1024)
            data = data.decode("utf-8")
            print(f"Received response: {data}")

