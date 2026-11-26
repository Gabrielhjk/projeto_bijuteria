from pydantic import BaseModel

class StageRequestDto(BaseModel):
    id: int
    stage: str