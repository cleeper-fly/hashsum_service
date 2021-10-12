from typing import Optional

from sqlmodel import SQLModel, Field


class Result(SQLModel, table=True):
    __tablename__ = 'result'

    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: str
    result_hash: str
