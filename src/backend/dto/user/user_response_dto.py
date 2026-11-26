from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserResponseDto(BaseModel):
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime