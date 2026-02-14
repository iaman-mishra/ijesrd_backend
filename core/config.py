from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from pydantic import Field
class Settings(BaseSettings):
    APP_NAME: str = "IJESRD-Server"
    APP_ENV: Literal["development", "staging", "production"] = "development"
    DEBUG: bool = True
    DB_URI: str = Field(default="")
    ALLOWED_ORIGINS : list[str] = ["http://localhost:3000"]
    ROUTE_PREFIX: str = "/api"
    model_config = SettingsConfigDict(env_file=".env")
    
    
settings = Settings()
