from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.user.user_model import User
from pydantic import EmailStr
from fastapi import HTTPException, status
from datetime import timedelta

from app.user.user_schema import CreateUserInput
from app.core.security import create_token


class UserServices:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def getUserByEmail(self, email: EmailStr):
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def sendVerificationEmail(self, email: EmailStr):
        try:
            pass
            tokendata = {"email": email}
            token = create_token(tokendata, timedelta(minutes=15))

        except Exception:
            pass

    async def create_user(self, data: CreateUserInput):
        try:

            result = await self.db.execute(select(User).where(User.email == data.email))
            existing_user = result.scalar_one_or_none()

            if existing_user:
                if existing_user.active:
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail="User already exists",
                    )
                else:
                    await self.sendVerificationEmail(email=existing_user.email)
                    return existing_user

            new_user = User(
                name=f"{data.firstName} {data.lastName}",
                email=data.email,
                password=data.password,
            )

            self.db.add(new_user)
            await self.db.commit()
            await self.db.refresh(new_user)

            return new_user

        except Exception:
            await self.db.rollback()
            raise
