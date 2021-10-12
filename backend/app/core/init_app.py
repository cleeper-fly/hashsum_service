from typing import Callable

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.apps import routes
from app.core.config import get_settings
from app.core.db import check_table_exists_and_create

config = get_settings()


def create_on_startup_handler(app: FastAPI) -> Callable:
    def on_startup():
        check_table_exists_and_create()
    return on_startup


def create_on_shutdown_handler(app: FastAPI) -> Callable:
    def on_shutdown():
        pass
    return on_shutdown


def init_middlewares(app: FastAPI) -> None:
    pass


def register_routers(app: FastAPI):
    """Регистрация роутеров FastAPI."""
    for router in routes.v1_routers:
        app.include_router(router, prefix=f'{config.API_PREFIX}/v1')


def register_events(app: FastAPI) -> None:
    app.add_event_handler('startup', create_on_startup_handler(app))
    app.add_event_handler('shutdown', create_on_shutdown_handler(app))
