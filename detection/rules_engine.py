import json
import os

class RulesEngine:
    def __init__(self, rules_path="data/rules.json"):
        self.rules_path = rules_path
        self.rules = []
        self._load_rules()

    def _load_rules(self):
        if not os.path.exists(self.rules_path):
            self.rules = []
            return

        try:
            with open(self.rules_path, "r") as f:
                data = json.load(f)
                self.rules = data.get("rules", [])
        except:
            self.rules = []

    def reload_rules(self):
        self._load_rules()

    def evaluate(self, packet_data):
        matches = []

        for rule in self.rules:
            if self._match_rule(rule, packet_data):
                matches.append(rule)

        return matches

    def _match_rule(self, rule, data):
        try:
            for key, value in rule.get("conditions", {}).items():
                if key not in data:
                    return False

                if isinstance(value, list):
                    if data[key] not in value:
                        return False
                else:
                    if data[key] != value:
                        return False

            return True
        except:
            return False
