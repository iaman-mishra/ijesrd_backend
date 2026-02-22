from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from uuid import UUID


class CreateUserInput(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)
    firstName: str
    lastName: str


class CreateUserOutput(BaseModel):
    uuid: UUID
    name: str
    email: EmailStr
    active: bool
    blocked: bool
    created_at: datetime
    updated_at: datetime
