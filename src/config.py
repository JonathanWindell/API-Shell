from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Define variables and types (str, int)

    secret_key: str = (
        "default_secret_for_dev_only"  # Standardvalue to protect against crash
    )
    algorithm: str = "HS256"
    # Pydantic translates to int
    access_token_expire_minutes: int = 30

    #
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
