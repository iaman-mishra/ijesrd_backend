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
   
    # CORS
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]

    # Security / JWT
    JWT_SECRET: str = Field(default="VERY_CONFIDENTIAL")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRY_MINUTES:int=30
    REFRESH_TOKEN_EXPIRY_DAYS:int=7

    # Environment File
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
