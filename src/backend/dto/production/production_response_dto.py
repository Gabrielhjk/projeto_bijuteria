from sqlalchemy import DateTime
from pydantic import BaseModel
from ...db.enums.status import StatusEnum

class ProductionResponseDto(BaseModel):
    product_id: int
    current_stage_id: int
    amount: int
    status: StatusEnum
    created_at: DateTime
    updated_at: DateTime
    completion_date: DateTime 