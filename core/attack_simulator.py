import random
import time

class AttackSimulator:
    def __init__(self):
        self.attacks = ["NORMAL", "SYN_FLOOD", "PORT_SCAN", "DDOS_SPIKE"]

    def generate_packet(self):

        #  throttle generation (prevents infinite spam)
        time.sleep(0.15)

        attack = random.choices(
            self.attacks,
            weights=[70, 12, 10, 8]
        )[0]

        if attack == "NORMAL":
            return {
                "type": "NORMAL",
                "src_ip": f"192.168.1.{random.randint(2, 200)}",
                "dst_ip": "8.8.8.8",
                "protocol": "TCP",
                "size": random.randint(60, 300)
            }

        if attack == "SYN_FLOOD":
            return {
                "type": "SYN_FLOOD",
                "src_ip": f"10.0.0.{random.randint(2, 50)}",
                "dst_ip": "8.8.8.8",
                "protocol": "TCP",
                "flag": "SYN",
                "size": 64
            }

        if attack == "PORT_SCAN":
            return {
                "type": "PORT_SCAN",
                "src_ip": f"172.16.0.{random.randint(2, 100)}",
                "dst_ip": "192.168.1.1",
                "protocol": "TCP",
                "port": random.randint(1, 1024)
            }

        return {
            "type": "DDOS_SPIKE",
            "src_ip": f"185.1.2.{random.randint(1, 255)}",
            "dst_ip": "8.8.8.8",
            "protocol": "UDP",
            "size": random.randint(800, 1500)
        }
