import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class AlertService:
    def __init__(self, config_path="config/settings.yaml"):
        self.config = self._load_config(config_path)

    def _load_config(self, path):
        try:
            import yaml
            with open(path, "r") as f:
                return yaml.safe_load(f)
        except:
            return {}

    def send_email_alert(self, subject, message):
        email_cfg = self.config.get("email", {})
        if not email_cfg:
            return False

        try:
            msg = MIMEMultipart()
            msg["From"] = email_cfg.get("from")
            msg["To"] = email_cfg.get("to")
            msg["Subject"] = subject

            msg.attach(MIMEText(message, "plain"))

            server = smtplib.SMTP(email_cfg.get("smtp_server"), email_cfg.get("smtp_port"))
            server.starttls()
            server.login(email_cfg.get("username"), email_cfg.get("password"))
            server.send_message(msg)
            server.quit()
            return True
        except:
            return False

    def send_webhook_alert(self, data):
        webhook_url = self.config.get("webhook_url")
        if not webhook_url:
            return False

        try:
            import requests
            headers = {"Content-Type": "application/json"}
            requests.post(webhook_url, data=json.dumps(data), headers=headers, timeout=5)
            return True
        except:
            return False

    def alert(self, threat, packet_data):
        subject = f"[IPS ALERT] {threat.get('reason')}"
        message = json.dumps({
            "threat": threat,
            "packet": packet_data
        }, indent=2)

        self.send_email_alert(subject, message)
        self.send_webhook_alert({
            "threat": threat,
            "packet": packet_data
        })
