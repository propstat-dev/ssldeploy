import os
import re
import glob
import platform
import subprocess
import threading
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# 1. Detect if we are running via `flask run`
def is_flask_dev():
    return os.environ.get("FLASK_RUN_FROM_CLI") == "true"

# 2. FORCE Debug mode always when using `flask run`
# Environment variables require strings, so we use the string "true"
if is_flask_dev():
    os.environ["FLASK_DEBUG"] = "true"

ssldeploy = Flask(__name__)
ssldeploy.config.from_object(Config)

# Initialize database and migration objects after app is created
db = SQLAlchemy(ssldeploy)
migrate = Migrate(ssldeploy, db)

# Flask configuration dicts require Python booleans, so we use True
if is_flask_dev():
    ssldeploy.config["DEBUG"] = True


def is_musl() -> bool:
    """Detect musl libc (e.g. Alpine) vs glibc (e.g. Ubuntu/Debian)."""
    try:
        result = subprocess.run(
            ["ldd", "--version"], capture_output=True, text=True
        )
        combined = (result.stdout + result.stderr).lower()
        return "musl" in combined
    except FileNotFoundError:
        # No ldd at all usually means musl-based (e.g. Alpine)
        return True


def get_tailwind_binary() -> str:
    """Pick the correct tailwindcss standalone CLI binary for the current
    OS/architecture/libc, automatically selecting the highest available
    version found in ./tools/tailwind.
    """
    system = platform.system().lower()       # 'linux', 'darwin', 'windows'
    machine = platform.machine().lower()      # 'x86_64', 'arm64', 'aarch64', etc.

    if machine in ("x86_64", "amd64"):
        arch = "x64"
    elif machine in ("arm64", "aarch64"):
        arch = "arm64"
    else:
        raise RuntimeError(f"Unsupported architecture: {machine}")

    if system == "darwin":
        prefix = f"tailwindcss-macos-{arch}"
        ext = ""
    elif system == "linux":
        musl_suffix = "-musl" if is_musl() else ""
        prefix = f"tailwindcss-linux-{arch}{musl_suffix}"
        ext = ""
    elif system == "windows":
        prefix = f"tailwindcss-windows-{arch}"
        ext = ".exe"
    else:
        raise RuntimeError(f"Unsupported OS: {system}")

    tailwind_dir = "./tools/tailwind"
    pattern = os.path.join(tailwind_dir, f"{prefix}-*{ext}")
    candidates = glob.glob(pattern)

    # Anchor the regex on the exact prefix so e.g. "linux-x64" doesn't
    # accidentally also match "linux-x64-musl" files.
    version_re = re.compile(
        rf"^{re.escape(prefix)}-v?(\d+){re.escape(ext)}$"
    )

    versioned = []
    for path in candidates:
        filename = os.path.basename(path)
        match = version_re.match(filename)
        if match:
            versioned.append((int(match.group(1)), path))

    if not versioned:
        raise FileNotFoundError(
            f"No Tailwind CLI binary found matching '{prefix}-*{ext}' in {tailwind_dir}"
        )

    versioned.sort(key=lambda x: x[0], reverse=True)
    return versioned[0][1]


def run_tailwind():
    binary = get_tailwind_binary()
    subprocess.run([
        binary,
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

from ssldeploy import routes, models