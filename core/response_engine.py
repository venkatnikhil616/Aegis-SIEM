from core.ai_engine import AIEngine
from core.event_store import EventStore

store = EventStore()

class ResponseEngine:
    def __init__(self):
        self.ai = AIEngine()

    def handle(self, threat, packet):

        label, score = self.ai.score(packet)

        # 🧠 IMPORTANT: always store event FIRST
        event = {
            "packet": packet,
            "threat": threat,
            "severity": label,
            "score": score
        }

        store.add_event(event)

        # 🚫 ignore low noise
        if score < 40:
            return

        print("\n" + "─" * 70)
        print("🚨 SIEM ALERT")
        print("─" * 70)
        print(f"TYPE     : {packet.get('type')}")
        print(f"SOURCE   : {packet.get('src_ip')}")
        print(f"SCORE    : {score}")
        print(f"SEVERITY : {label}")
        print("─" * 70)
