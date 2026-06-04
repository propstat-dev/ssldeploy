import os
import subprocess
import threading
from flask import Flask
from config import Config

# 1. Detect if we are running via `flask run`
def is_flask_dev():
    return os.environ.get("FLASK_RUN_FROM_CLI") == "true"

# 2. FORCE Debug mode always when using `flask run`
# Environment variables require strings, so we use the string "true"
if is_flask_dev():
    os.environ["FLASK_DEBUG"] = "true"

ssldeploy = Flask(__name__)
ssldeploy.config.from_object(Config)

# Flask configuration dicts require Python booleans, so we use True
if is_flask_dev():
    ssldeploy.config["DEBUG"] = True

def run_tailwind():
    subprocess.run([
        "./tools/tailwind/tailwindcss-macos-arm64-v430",
        "-i", "./tools/tailwind/input.css",
        "-o", "./ssldeploy/static/css/ssldeploy.css",
        "--watch"
    ])

def start_tailwind_if_dev():
    if is_flask_dev():
        # Werkzeug sets this to the string "true" when the main reloader process boots
        if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            t = threading.Thread(target=run_tailwind)
            t.daemon = True
            t.start()

# Start Tailwind (guarded to only run during `flask run` + main reloader thread)
start_tailwind_if_dev()

# Clean logging blocks
if is_flask_dev():
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        ssldeploy.logger.info("⚡ Dev mode: Tailwind + Flask debug enabled")
else:
    # Gunicorn ignores WERKZEUG_RUN_MAIN and lands safely here
    ssldeploy.logger.info("🚀 Production mode: Gunicorn active (Tailwind disabled)")

from ssldeploy import routes