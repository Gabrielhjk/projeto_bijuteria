from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserUpdateDto(BaseModel):
    name: str
    email: EmailStr
    password: str
    created_at: datetime
    updated_at: datetime