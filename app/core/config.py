from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from pydantic import Field


class Settings(BaseSettings):

    # App Configuration
    APP_NAME: str = "IJESRD-Server"
    ROUTE_PREFIX: str = "/api"
    APP_ENV: Literal["development", "staging", "production"] = "development"
    DEBUG: bool = True

    # Database
    DB_URI: str = Field(default="")

    # FE Url
    FE_URL: str = "http://localhost:3000"

    # CORS
    @property
    def ALLOWED_ORIGINS(self) -> list[str]:
        return [self.FE_URL]

    # Security / JWT
    JWT_SECRET: str = Field(default="VERY_CONFIDENTIAL")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRY_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRY_DAYS: int = 7

    # Email
    MAIL_USERNAME: str = ""
    MAIL_PASSWORD: str = ""
    MAIL_FROM: str = ""
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_FROM_NAME: str = "IJESRD"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
