import os
from environs import Env

env_file = os.getenv('GUNICORN_ENV_FILE', '.env')

env = Env()
env.read_env()


host = env('HOST', '0.0.0.0')
port = env('PORT', 8000)
use_bind = f'{host}:{port}'
max_workers = env('MAX_WORKERS', 2)
bind = use_bind

graceful_timeout = env.int('GRACEFUL_TIMEOUT', 120)
timeout = env.int('TIMEOUT', 120)
keepalive = env.int('KEEP_ALIVE', 5)
