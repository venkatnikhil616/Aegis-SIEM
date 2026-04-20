import json
import time
import requests

class ThreatIntelService:
    def __init__(self, blacklist_path="data/blacklist.json", update_interval=3600):
        self.blacklist_path = blacklist_path
        self.update_interval = update_interval
        self.blacklist = set()
        self.last_updated = 0

        self.sources = [
            "https://feodotracker.abuse.ch/downloads/ipblocklist.json",
            "https://rules.emergingthreats.net/blockrules/compromised-ips.txt"
        ]

        self._load_local_blacklist()

    def _load_local_blacklist(self):
        try:
            with open(self.blacklist_path, "r") as f:
                data = json.load(f)
                self.blacklist.update(data.get("ips", []))
        except:
            pass

    def _save_blacklist(self):
        try:
            with open(self.blacklist_path, "w") as f:
                json.dump({"ips": list(self.blacklist)}, f, indent=2)
        except:
            pass

    def _fetch_json_source(self, url):
        try:
            res = requests.get(url, timeout=10)
            data = res.json()
            ips = set()

            for entry in data:
                ip = entry.get("ip_address") or entry.get("ip")
                if ip:
                    ips.add(ip)

            return ips
        except:
            return set()

    def _fetch_text_source(self, url):
        try:
            res = requests.get(url, timeout=10)
            lines = res.text.splitlines()
            ips = set()

            for line in lines:
                line = line.strip()
                if line and not line.startswith("#"):
                    ips.add(line)

            return ips
        except:
            return set()

    def update_blacklist(self):
        new_ips = set()

        for source in self.sources:
            if source.endswith(".json"):
                new_ips.update(self._fetch_json_source(source))
            else:
                new_ips.update(self._fetch_text_source(source))

        if new_ips:
            self.blacklist.update(new_ips)
            self._save_blacklist()
            self.last_updated = time.time()

    def get_blacklist(self):
        if time.time() - self.last_updated > self.update_interval:
            self.update_blacklist()
        return self.blacklist

    def is_malicious(self, ip):
        return ip in self.get_blacklist()
