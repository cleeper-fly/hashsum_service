from pathlib import Path
from shutil import copyfileobj
from uuid import uuid4

from fastapi import UploadFile

from app.core.config import get_settings

settings = get_settings()


def copy_file_to_tmp(upload_file: UploadFile) -> Path:
    full_temp_file_path = Path(f'{settings.file_storage}/{str(uuid4())}')
    with open(full_temp_file_path, 'wb') as fi:
        copyfileobj(upload_file.file, fi)
    return full_temp_file_path
