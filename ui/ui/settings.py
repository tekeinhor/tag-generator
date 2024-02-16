"""Configuration file for settings and env variables."""
from pydantic_settings import BaseSettings


class UISettings(BaseSettings):  # type: ignore # conflict between mypy v1.8 and pydantic
    """Contains all API settings."""

    ENV: str | None = "dev"

    # SERVER
    API_ENDPOINT_URL: str = "http://localhost:8080/api/v1/predict"


settings = UISettings()
