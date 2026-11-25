from sqlalchemy import DateTime
from pydantic import BaseModel

class productResponseDto(BaseModel):
    product_name: str
    product_code: str
    description: str | None
    active: bool
    created_at: DateTime
    updated_at: DateTime
    