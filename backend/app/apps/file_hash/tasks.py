import hashlib
from pathlib import Path

from sqlmodel import Session
from app.apps.file_hash.models import Result
from app.core.celery import celery
from app.core.db import engine


def get_file_checksum(filepath: str) -> str:
    file_hash = hashlib.md5()
    with open(Path(filepath), 'rb') as file:
        while chunk := file.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()


@celery.task(name='count_md5_file_hashsum')
def count_md5_sum(filepath: str) -> None:
    md5_sum = get_file_checksum(filepath)
    result = Result(
        task_id=count_md5_sum.request.id,
        result_hash=md5_sum,
    )
    with Session(engine) as session:
        session.add(result)
        session.commit()



