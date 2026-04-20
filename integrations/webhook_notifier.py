import json
import requests

class WebhookNotifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send(self, data):
        try:
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                self.webhook_url,
                data=json.dumps(data),
                headers=headers,
                timeout=5
            )
            return response.status_code in (200, 201, 202)
        except:
            return False
