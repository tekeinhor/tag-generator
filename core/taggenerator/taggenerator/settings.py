"""Configuration file for settings and env variables."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):  # type: ignore # conflict between pydantic and mypy v1.8
    """Contains all API settings."""

    ENV: str | None = "dev"
    NLTK_DATA_DIR: str | None = None


settings = Settings()
