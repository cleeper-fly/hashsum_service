from celery import Celery

from app.core.config import get_settings
from app.core.db import check_table_exists_and_create

settings = get_settings()

celery = Celery(__name__)
celery.conf.broker_url = settings.CELERY_BROKER_URL
celery.conf.task_serializer = 'json'

celery.autodiscover_tasks(['app.apps.file_hash'])
check_table_exists_and_create()
