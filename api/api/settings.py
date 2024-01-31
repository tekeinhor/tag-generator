"""Configuration file for settings and env variables."""
from pydantic_settings import BaseSettings


class APISettings(BaseSettings):  # type: ignore # conflict between pydantic and mypy v1.8
    """Contains all API settings."""

    ENV: str | None = "dev"

    # SERVER
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8080

    # API
    API_PREFIX: str = "/api/v1"
    API_NAME: str = "tag-generator"
    API_TITLE: str = "Tag Generator"
    API_SUMMARY: str = "Tag Generator API"
    API_DESCRIPTION: str = "Tag generator for stackoverflow questions using a multiclass model for predictions."

    # MODEL
    LOCAL_MODEL_PATH_DIR: str = ""
    S3_MODEL_BUCKET: str = "tek-tag-generator-dev"
    S3_MODEL_KEY: str = "models/2024-01-02/19/193120_final_so_questions_2008_2023_artifacts_v1.0.0.pkl"
    S3_SESSION_PROFILE: str = "tek-tatiana"


settings = APISettings()
