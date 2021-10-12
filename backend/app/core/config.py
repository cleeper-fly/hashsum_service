from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings, SecretStr

PROJECT_ROOT = Path(__file__).parent.parent
BASE_DIR = PROJECT_ROOT.parent


class AppSettings(BaseSettings):
    """Настройки сервиса."""

    class Config(object):
        env_file = BASE_DIR.joinpath('.env')
        env_file_encoding = 'utf-8'
        use_enum_values = True

    # App
    APP_NAME: str = 'file_hash'
    SECRET_KEY: SecretStr = 'secret'

    DB_URL: str
    CELERY_BROKER_URL: str

    DEBUG: bool = True

    API_PREFIX: str = '/api'
    AUTO_RELOAD: bool = False
    HOST: str = '127.0.0.1'
    PORT: int = 8000
    WEB_CONCURRENCY: int = 1

    APPLICATIONS_MODULE: str = 'app.apps'
    APPLICATIONS: tuple[str, ...] = (
        'file_hash',
    )

    file_storage: str = '/tmp/'


@lru_cache
def get_settings() -> AppSettings:
    """Получение настроек сервиса."""
    return AppSettings()
