import secrets
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_ignore_empty=True,
        extra="ignore",
    )
    SECRET_KEY: str = secrets.token_urlsafe(32)

    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    DATABASE_URI: str = "sqlite:///test.db"


settings = Settings()  # type: ignore
