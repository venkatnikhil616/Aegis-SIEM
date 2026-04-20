import time
from core.listener import Listener

def banner():
    print("""
============================================================
                 🛡️ AEGIS SIEM PLATFORM
        AI-POWERED THREAT DETECTION & RESPONSE ENGINE
============================================================
""")


def main():
    banner()

    print("[INIT] Starting AI detection engine...\n")

    # 🚀 NEW ARCHITECTURE ENTRY POINT
    engine = Listener()
    engine.start()

    # keep process alive (optional depending on listener loop)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] AegisSIEM stopped safely.")


if __name__ == "__main__":
    main()
