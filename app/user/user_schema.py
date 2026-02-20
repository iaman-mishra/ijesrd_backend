from pydantic import BaseModel, Field , EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=8)


class UserResponse(UserBase):
    id: int
    active: bool
    blocked: bool
    image: Optional[str] = None

    class Config:
        from_attributes = True
