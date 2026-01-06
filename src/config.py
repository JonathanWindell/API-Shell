from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from src.config import settings


class Settings(BaseSettings):
    # Define variables and types (str, int)

    secret_key: str = (
        "default_secret_for_dev_only"  # Standardvalue to protect against crash
    )
    algorithm: str = "HS256"
    # Pydantic translates to int
    access_token_expire_minutes: int = 30

    SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
