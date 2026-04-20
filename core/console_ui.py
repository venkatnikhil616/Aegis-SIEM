import time
import sys

class ConsoleUI:
    @staticmethod
    def banner():
        print("\n" + "=" * 60)
        print("        ENFORCER IPS - LIVE PROTECTION ENGINE")
        print("=" * 60 + "\n")

    @staticmethod
    def packet(packet):
        print(f"[PACKET] {packet}")

    @staticmethod
    def threat(threat):
        print("\033[91m" + f"[THREAT] 🚨 {threat}" + "\033[0m")

    @staticmethod
    def blocked(ip, reason):
        print("\033[93m" + f"[BLOCKED] ⛔ {ip} -> {reason}" + "\033[0m")

    @staticmethod
    def status(msg):
        print("\033[92m" + f"[STATUS] {msg}" + "\033[0m")

    @staticmethod
    def loading(text, seconds=1):
        for i in range(seconds * 3):
            sys.stdout.write(f"\r{text}{'.' * (i % 4)}   ")
            sys.stdout.flush()
            time.sleep(0.3)
        print("\n")
