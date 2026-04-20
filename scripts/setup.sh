#!/bin/bash

set -e

echo "Setting up Enforcer IPS..."

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

mkdir -p logs
mkdir -p data
mkdir -p reports

touch logs/activity.log
touch logs/alerts.log
touch logs/errors.log

chmod +x scripts/run.sh

echo "Setup complete."
echo "Activate environment: source venv/bin/activate"
echo "Run project: ./scripts/run.sh"
