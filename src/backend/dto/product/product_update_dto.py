from sqlalchemy import Boolean, DateTime
from pydantic import BaseModel

class ProductUpdateDto(BaseModel):
    product_name: str
    product_code: str
    description: str | None
    active: Boolean
    created_at: DateTime
    updated_at: DateTime
    