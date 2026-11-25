from pydantic import BaseModel

class stageRequestDto(BaseModel):
    id: int
    stage: str