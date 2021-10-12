from pydantic import BaseModel


class ResultResponseRequestDTO(BaseModel):
    task_id: str
