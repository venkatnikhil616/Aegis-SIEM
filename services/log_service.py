import logging
import os

class LogService:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

        self.activity_logger = self._setup_logger("activity", "activity.log")
        self.alert_logger = self._setup_logger("alerts", "alerts.log")
        self.error_logger = self._setup_logger("errors", "errors.log")

    def _setup_logger(self, name, filename):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        file_path = os.path.join(self.log_dir, filename)

        if not logger.handlers:
            file_handler = logging.FileHandler(file_path)
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger

    def log_activity(self, message):
        self.activity_logger.info(message)

    def log_alert(self, message):
        self.alert_logger.warning(message)

    def log_error(self, message):
        self.error_logger.error(message)
