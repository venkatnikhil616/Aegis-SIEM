import time
import random
from queue import Queue

class PacketSource:
    def __init__(self, queue: Queue):
        self.queue = queue
        self.running = False

    def start(self):
        self.running = True
        print("[+] Mobile Packet Source started")

        while self.running:
            packet = self.generate_packet()
            self.queue.put(packet)
            time.sleep(1)

    def stop(self):
        self.running = False

    def generate_packet(self):
        return {
            "src_ip": f"192.168.1.{random.randint(2, 200)}",
            "dst_ip": "8.8.8.8",
            "protocol": random.choice(["TCP", "UDP", "ICMP"]),
            "size": random.randint(64, 1500),
            "flag": random.choice(["SYN", "ACK", "NONE"])
        }
