# core/security.py

from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt
from passlib.context import CryptContext

from core.config import settings

# ─────────────────────────────────────────────
# Password Hashing (bcrypt via passlib)
# ─────────────────────────────────────────────

pwd_context = CryptContext( schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# ─────────────────────────────────────────────
# JWT Token Creation
# ─────────────────────────────────────────────

def _create_token(data: dict[str, Any], expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
   
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


def create_access_token(subject: str | int) -> str:
    return _create_token(
        {
            "sub": str(subject),
            "type": "access",
        },
        timedelta(minutes=settings.ACCESS_TOKEN_EXPIRY_MINUTES),
    )


def create_refresh_token(subject: str | int) -> str:
    return _create_token(
        {
            "sub": str(subject),
            "type": "refresh",
        },
        timedelta(days=settings.REFRESH_TOKEN_EXPIRY_DAYS)
    )


# ─────────────────────────────────────────────
# Token Decode / Verify
# ─────────────────────────────────────────────
def decode_token(token: str) -> dict[str, Any]:
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
