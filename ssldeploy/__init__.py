import os
import subprocess
import threading
from flask import Flask

ssldeploy = Flask(__name__)

def run_tailwind():
    subprocess.run([
        "./tools/tailwindcss",
        "-i", "./src/input.css",
        "-o", "./static/css/output.css",
        "--watch"
    ])

def is_flask_dev():
    return os.environ.get("FLASK_RUN_FROM_CLI") == "true"

def start_tailwind_if_dev():
    if is_flask_dev():
        # Only run once (avoid reloader duplication)
        if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            t = threading.Thread(target=run_tailwind)
            t.daemon = True
            t.start()

# 🔥 Force debug mode if using `flask run`
if is_flask_dev():
    ssldeploy.config["DEBUG"] = True

start_tailwind_if_dev()

if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    if is_flask_dev():
        ssldeploy.logger.info("⚡ Dev mode: Tailwind + Flask debug enabled")
    else:
        ssldeploy.logger.info("🚀 Production mode: Gunicorn expected")

from ssldeploy import routes