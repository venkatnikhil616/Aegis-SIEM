import os
from core.event_store import EventStore
from collections import Counter

class SOCDashboard:
    def __init__(self):
        # ⚠️ IMPORTANT: singleton EventStore (shared across system)
        self.store = EventStore()

    def render(self):
        os.system("clear")

        events = self.store.get_recent(100)

        print("=" * 70)
        print("🛡️ AEGIS SIEM - SECURITY OPERATIONS CENTER DASHBOARD")
        print("=" * 70)

        self._stats(events)
        self._top_sources(events)
        self._severity_distribution(events)

        print("\n" + "=" * 70)

    # 📊 EVENT COUNT
    def _stats(self, events):
        print(f"\n📊 EVENT COUNT: {len(events)}")

    # 🔥 TOP SOURCES
    def _top_sources(self, events):
        counter = Counter()

        for e in events:
            packet = e.get("packet", {})
            src = packet.get("src_ip")
            if src:
                counter[src] += 1

        print("\n🔥 TOP SOURCES:")

        if not counter:
            print("No data")
            return

        for ip, count in counter.most_common(5):
            print(f"{ip:<20} {count}")

    # 🚨 SEVERITY DISTRIBUTION
    def _severity_distribution(self, events):
        counter = Counter()

        for e in events:
            sev = e.get("severity")
            if sev:
                counter[sev] += 1

        print("\n🚨 SEVERITY DISTRIBUTION:")

        if not counter:
            print("No data")
            return

        for k, v in counter.items():
            print(f"{k:<10}: {v}")
