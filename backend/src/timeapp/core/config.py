"""Environment-backed application settings."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings loaded from environment variables or a local .env file."""

    app_name: str = "TimeApp"
    environment: str = "development"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="TIMEAPP_",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return one settings instance per process."""

    return Settings()
