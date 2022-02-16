# This is a copy of:
# https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/docker-images/gunicorn_conf.py
#
# Changes are added to the end of this file. Whenever you update the
# base docker-image check if you need to update this config-file as well.

import json
import os
import dotenv
dotenv.load_dotenv(".env")

host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("APP_PORT", "80")

bind_env = os.getenv("BIND", None)
use_loglevel = os.getenv("LOG_LEVEL", "info")
if bind_env:
    use_bind = bind_env
else:
    use_bind = f"{host}:{port}"

accesslog_var = os.getenv("ACCESS_LOG", "-")
use_accesslog = accesslog_var or None
errorlog_var = os.getenv("ERROR_LOG", "-")
use_errorlog = errorlog_var or None
graceful_timeout_str = os.getenv("GRACEFUL_TIMEOUT", "120")
timeout_str = os.getenv("TIMEOUT", "120")
keepalive_str = os.getenv("KEEP_ALIVE", "5")

# Gunicorn config variables.
loglevel = use_loglevel
workers = 1
bind = use_bind
errorlog = use_errorlog
worker_tmp_dir = "/dev/shm"
accesslog = use_accesslog
graceful_timeout = int(graceful_timeout_str)
timeout = int(timeout_str)
keepalive = int(keepalive_str)


# For debugging and testing.
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    "graceful_timeout": graceful_timeout,
    "timeout": timeout,
    "keepalive": keepalive,
    "errorlog": errorlog,
    "accesslog": accesslog,
    # Additional, non-gunicorn variables
    "workers_per_core": 1,
    "use_max_workers": None,
    "host": host,
    "port": port,
}
print(json.dumps(log_data))


# --- Add your changes after this line ---
from app.config import LOGGING_CONFIG
logconfig_dict = LOGGING_CONFIG
