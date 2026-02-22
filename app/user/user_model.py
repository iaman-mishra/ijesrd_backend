from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, validates

from app.core.database import Base
from app.core.mixins import TimestampMixin, UUIDMixin
from app.core.security import hash_password


class User(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String, nullable=False)

    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)

    password: Mapped[str] = mapped_column(nullable=False)

    active: Mapped[bool] = mapped_column(Boolean, default=False)

    blocked: Mapped[bool] = mapped_column(Boolean, default=False)

    blockReason: Mapped[str] = mapped_column(String, nullable=True, default=None)

    refreshToken: Mapped[str] = mapped_column(String, nullable=True, default=None)

    image: Mapped[str] = mapped_column(String, nullable=True, default=None)

    @validates("password")
    def hash_user_password(self, key, value):
        if value.startswith("$2b$"):
            return value
        return hash_password(value)
