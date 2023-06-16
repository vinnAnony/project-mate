#!/bin/bash
APP_PORT=${PORT:-8111}
cd /app/
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm bizcore.wsgi:application --bind "0.0.0.0:${APP_PORT}"
