from sqlalchemy import Boolean, DateTime
from pydantic import BaseModel

class ProductRequestDto(BaseModel):
    id: int
    product_name: str
    product_code: str
    description: str | None
    created_at: DateTime
    updated_at: DateTime
    