from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.user.user_model import User
from pydantic import EmailStr
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

from app.user.user_schema import CreateUserInput
from app.core.security import create_token
from app.core.email import send_email
from app.core.config import settings


class UserServices:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_email(self, email: EmailStr):
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def send_verification_email(self, email: EmailStr, name: str):
        token = create_token({"email": email})

        await send_email(
            recipients=[email],
            subject="IJESRD Account Verification",
            template_name="verify_email.html",
            template_body={
                "name": f"{name}",
                "verification_url": f"{settings.FE_URL}/verify?token={token}",
            },
        )

    async def create_user(self, data: CreateUserInput):

        existing_user = await self.get_user_by_email(data.email)

        if existing_user:
            if existing_user.active:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="User already exists",
                )
            else:
                await self.send_verification_email(
                    existing_user.email, existing_user.name
                )
                return existing_user

        new_user = User(
            name=f"{data.firstName} {data.lastName}",
            email=data.email,
            password=data.password,
        )

        try:
            self.db.add(new_user)
            await self.db.commit()
            await self.db.refresh(new_user)

        except IntegrityError:
            await self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Database Integrigrity Error",
            )

        await self.send_verification_email(new_user.email, new_user.name)

        return new_user
