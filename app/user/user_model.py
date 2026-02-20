from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column , validates

from core.database import Base
from core.mixins import TimestampMixin ,UUIDMixin
from core.security import hash_password


class User(Base, UUIDMixin, TimestampMixin ):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    email: Mapped[str] = mapped_column(
        unique=True,
        index=True,
        nullable=False
    )
    
    password: Mapped[str] = mapped_column(
        nullable=False
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
    
    blocked:Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )
    
    blockReason:Mapped[str] = mapped_column(
        String,
        default="",
        nullable=False,
    )
    
    refreshToken: Mapped[str] = mapped_column(
        String,
        nullable=True,
        default=None
    )
    
    image: Mapped[str] = mapped_column(
        String,
         nullable=True,
         default=None
    )

    @validates("password")
    def hash_user_password(self):
        if self.password.startswith("$2b$"):
            return self.password
        return hash_password(self.password)