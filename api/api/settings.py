from pydantic import BaseSettings


class APISettings(BaseSettings):
    ENV: str | None = "dev"

    # SERVER
    SERVER_HOST: str = "dev"
    SERVER_PORT: int = 8080

    # API
    API_PREFIX: str = "/api/v1"
    API_NAME: str = "tag-generator"
    API_TITLE: str = "Tag Generator"
    API_DESCRIPTION: str = "Tag generator for stackoverflow questions using a multiclass model for predictions."


settings = APISettings()
