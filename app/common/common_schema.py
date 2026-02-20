from pydantic import BaseModel
from typing import Optional, Generic, TypeVar

T = TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T] = None
    
class ErrorResponse(APIResponse, T = TypeVar("T") ):
    error_code: int