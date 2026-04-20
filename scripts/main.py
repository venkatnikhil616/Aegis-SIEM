#!/bin/bash

set -e

echo "Starting Enforcer IPS..."

if [ -d "venv" ]; then
    source venv/bin/activate
fi

python3 main.py
