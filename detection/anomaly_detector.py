import time
from collections import defaultdict, deque
import statistics

class AnomalyDetector:
    def __init__(self, window_size=50, threshold=3):
        self.window_size = window_size
        self.threshold = threshold
        self.traffic_history = defaultdict(lambda: deque(maxlen=self.window_size))

    def analyze(self, packet_data):
        src_ip = packet_data.get("src_ip")
        current_time = time.time()

        history = self.traffic_history[src_ip]
        history.append(current_time)

        if len(history) < 5:
            return {"anomalous": False}

        intervals = [
            history[i] - history[i - 1]
            for i in range(1, len(history))
        ]

        if not intervals:
            return {"anomalous": False}

        mean = statistics.mean(intervals)
        stdev = statistics.stdev(intervals) if len(intervals) > 1 else 0

        if stdev == 0:
            return {"anomalous": False}

        latest_interval = intervals[-1]
        z_score = abs((latest_interval - mean) / stdev)

        if z_score > self.threshold:
            return {
                "anomalous": True,
                "reason": "TRAFFIC_ANOMALY",
                "src_ip": src_ip,
                "z_score": z_score,
                "timestamp": current_time
            }

        return {"anomalous": False}
