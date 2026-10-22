from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    environment: str = "local"
    database_url: str = "sqlite:///./agent-service.db"
    internal_api_key: str = "development-only-key"
    default_image_provider: str = "fake"
    default_image_model: str = "fake-drawing-v1"


@lru_cache
def get_settings() -> Settings:
    return Settings()
