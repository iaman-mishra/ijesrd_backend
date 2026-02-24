from app.core.database import get_db
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.schema import APIResponse

from app.user.user_services import UserServices
from app.user.user_schema import CreateUserInput, CreateUserOutput


router = APIRouter(prefix="/user", tags=["User"])


@router.get("")
async def getUser():
    return {"sucess": True}


@router.post("/signup", response_model=APIResponse[CreateUserOutput])
async def register(body: CreateUserInput, db: AsyncSession = Depends(get_db)):
    service = UserServices(db)

    result = await service.create_user(body)

    return APIResponse(
        success=True,
        message="User registered successfully",
        data=result,
    )
