import uvicorn
from fastapi import FastAPI

from app.core.config import get_settings
from app.core.init_app import init_middlewares, register_routers, register_events

config = get_settings()


def create_app() -> FastAPI:
    app = FastAPI(title=config.APP_NAME)
    init_middlewares(app)
    register_routers(app)
    register_events(app)

    return app


if __name__ == '__main__':
    _config = uvicorn.Config(
        app='main:create_app',
        factory=True,
        host=config.HOST,
        port=config.PORT,
        reload=config.AUTO_RELOAD,
        workers=config.WEB_CONCURRENCY,
    )
    server = uvicorn.Server(_config)
    server.run()
