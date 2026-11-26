from pydantic import BaseModel

class StageUpdateDto(BaseModel):
    stage: str