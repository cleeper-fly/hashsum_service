from typing import Optional

from fastapi import APIRouter, status, HTTPException, UploadFile, File
from fastapi.responses import ORJSONResponse
from sqlmodel import Session, select

from app.apps.file_hash.dtos import ResultResponseRequestDTO
from app.apps.file_hash.helpers import copy_file_to_tmp
from app.apps.file_hash.models import Result
from app.apps.file_hash.tasks import count_md5_sum
from app.core.db import engine

router = APIRouter(
    prefix='/hash',
    tags=['file_hash'],
    default_response_class=ORJSONResponse,
)


@router.get('/get-result/{task_id}', response_model=Result, status_code=status.HTTP_200_OK)
def get_result(task_id: str) -> Optional[Result]:
    with Session(engine) as session:
        statement = select(Result).where(Result.task_id == task_id)
        results = session.exec(statement)
        if result := results.one_or_none():
            return result
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No task with such ID found.')


@router.post('/calculate-file-hash', response_model=ResultResponseRequestDTO, status_code=status.HTTP_201_CREATED)
def add_hash_task(
    uploaded_file: UploadFile = File(...)
) -> ORJSONResponse:
    task = count_md5_sum.apply_async(kwargs={'filepath': str(copy_file_to_tmp(uploaded_file))})
    return ORJSONResponse({'task_id': task.id})
