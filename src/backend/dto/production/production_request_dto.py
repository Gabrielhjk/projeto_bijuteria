from sqlalchemy import DateTime
from pydantic import BaseModel
from ...db.enums.status import statusEnum

class productionRequestDto(BaseModel):
    id: int
    product_id: int
    current_stage_id: int
    amount: int
    status: statusEnum
    created_at: DateTime
    updated_at: DateTime
    completion_date: DateTime 