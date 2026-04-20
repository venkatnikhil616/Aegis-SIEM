🛡️ Aegis-SIEM

An enterprise-style Security Information and Event Management (SIEM) and Intrusion Prevention System (IPS) built in Python.
Aegis-SIEM performs real-time event collection, detection, correlation, and automated response to security threats.

---

🚀 Overview

Aegis-SIEM simulates a Security Operations Center (SOC) pipeline by integrating:

- 📡 Network traffic monitoring
- 🧠 Detection engines (anomaly + signature + rule-based)
- 🔗 Event correlation
- 🚫 Intrusion prevention (firewall response)
- 📊 Web dashboard for visualization
- 🔔 Alerting & integrations

---

🔥 Key Features

- 📥 Log & event ingestion system
- 📡 Packet sniffing & traffic analysis
- 🧠 AI-based anomaly detection engine
- 📜 Signature & rule-based detection
- 🔗 Multi-event correlation engine
- 🚫 Automated response (IPS / firewall actions)
- 🌐 Web-based SOC dashboard
- 📊 Event storage & threat intelligence
- 🔔 Alerts via email / webhook
- 🧪 Attack simulation support

---

🧠 Architecture

Packet Source / Logs
        ↓
   Parser Engine
        ↓
 Detection Engines
 (Anomaly / Signature / Rules)
        ↓
 Correlation Engine
        ↓
 Response Engine (IPS / Firewall)
        ↓
 Event Store + Dashboard + Alerts

---

📁 Project Structure

enforcer-ips/
│
├── api/
│   ├── app.py
│   ├── auth.py
│   └── routes.py
│
├── config/
│   ├── config.py
│   ├── logging.conf
│   └── settings.yaml
│
├── core/
│   ├── ai_engine.py
│   ├── attack_simulator.py
│   ├── correlation_engine.py
│   ├── detector.py
│   ├── event_store.py
│   ├── firewall.py
│   ├── listener.py
│   ├── packet_sniffer.py
│   ├── packet_source.py
│   ├── parser.py
│   ├── response_engine.py
│   ├── scheduler.py
│   ├── shared_state.py
│   └── soc_dashboard.py
│
├── dashboard/
│   ├── app.py
│   ├── static/
│   └── templates/
│
├── data/
│   ├── blacklist.json
│   ├── geoip.db
│   ├── signatures.json
│   └── whitelist.conf
│
├── detection/
│   ├── anomaly_detector.py
│   ├── rate_limiter.py
│   ├── rules_engine.py
│   └── signature_detector.py
│
├── docker/
│   └── docker-compose.yaml
│
├── docs/
│   ├── api_docs.md
│   ├── architecture.md
│   └── usage.md
│
├── integrations/
│   ├── email_notifier.py
│   ├── firewall_adapter.py
│   ├── siem_exporter.py
│   └── webhook_notifier.py
│
├── scripts/
│   ├── run.sh
│   ├── setup.sh
│   └── simulate_attack.py
│
├── services/
│   ├── alert_service.py
│   ├── ips_service.py
│   ├── log_service.py
│   ├── report_service.py
│   └── threat_intel_service.py
│
├── tests/
│   ├── test_api.py
│   ├── test_detector.py
│   ├── test_firewall.py
│   └── test_parser.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

---

⚙️ Installation & Setup

1️⃣ Clone Repository

git clone <your-repo-url>
cd enforcer-ips

---

2️⃣ Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

---

3️⃣ Install Dependencies

pip install -r requirements.txt --break-system-packages

---

4️⃣ Configure Settings

Edit:

config/settings.yaml

Set:

- ports
- logging level
- detection thresholds

---

5️⃣ Run the System

python main.py

---


🧪 Simulate Attacks

python scripts/simulate_attack.py

This helps test:

- detection engine
- correlation
- alert generation

---

🔔 Alerts & Response

- Email notifications
- Webhook alerts
- Firewall blocking (IPS mode)

---

🐳 Docker Support

docker-compose up --build

---

🧠 Technologies Used

- Python
- Flask (Dashboard/API)
- Scapy (packet analysis)
- SQLite / JSON (storage)
- psutil (system monitoring)

---

🎯 Use Cases

- SOC simulation
- Intrusion detection & prevention
- Security research & learning
- Threat monitoring pipeline

---

⚠️ Disclaimer

This project is for educational and research purposes only.
Do not use in production environments without proper security validation.

---

👨‍💻 Author

Developed as part of advanced cybersecurity projects focusing on SIEM, IPS, and threat detection systems.

---

⭐ Future Improvements

- Machine learning-based threat detection
- Distributed log collection
- Cloud deployment
- Advanced visualization dashboards

---
