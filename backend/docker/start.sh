#! /usr/bin/env sh
set -e
# Start Gunicorn
exec gunicorn -k "uvicorn.workers.UvicornWorker" -c "/gunicorn.conf.py" "app.main:create_app"