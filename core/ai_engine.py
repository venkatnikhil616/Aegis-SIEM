class AIEngine:
    def __init__(self):
        self.ip_score_map = {}

    def score(self, packet):
        score = 0

        t = packet.get("type")

        if t == "NORMAL":
            score = 5
        elif t == "SYN_FLOOD":
            score = 60
        elif t == "PORT_SCAN":
            score = 50
        elif t == "DDOS_SPIKE":
            score = 85

        ip = packet.get("src_ip")
        if ip:
            self.ip_score_map[ip] = self.ip_score_map.get(ip, 0) + 3
            score += self.ip_score_map[ip]

        score = min(score, 100)

        if score < 30:
            return "LOW", score
        elif score < 60:
            return "MEDIUM", score
        elif score < 85:
            return "HIGH", score
        else:
            return "CRITICAL", score
