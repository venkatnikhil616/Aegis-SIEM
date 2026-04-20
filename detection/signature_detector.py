import json
import os
import re

class SignatureDetector:
    def __init__(self, signatures_path="data/signatures.json"):
        self.signatures_path = signatures_path
        self.signatures = []
        self._load_signatures()

    def _load_signatures(self):
        if not os.path.exists(self.signatures_path):
            self.signatures = []
            return

        try:
            with open(self.signatures_path, "r") as f:
                data = json.load(f)
                self.signatures = data.get("signatures", [])
        except:
            self.signatures = []

    def reload_signatures(self):
        self._load_signatures()

    def analyze(self, packet_data):
        matches = []

        for sig in self.signatures:
            if self._match_signature(sig, packet_data):
                matches.append(sig)

        if matches:
            return {
                "malicious": True,
                "reason": "SIGNATURE_MATCH",
                "matches": matches,
                "src_ip": packet_data.get("src_ip")
            }

        return {"malicious": False}

    def _match_signature(self, sig, data):
        try:
            conditions = sig.get("conditions", {})

            for key, pattern in conditions.items():
                value = str(data.get(key, ""))

                if sig.get("type") == "regex":
                    if not re.search(pattern, value):
                        return False
                else:
                    if value != str(pattern):
                        return False

            return True
        except:
            return False
