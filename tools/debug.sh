#!/bin/bash

# Go to project root (one level up from tools/)
cd "$(dirname "$0")/.."

# Activate venv + run Flask
source venv/bin/activate
export FLASK_APP=ssldeploy.py
flask run