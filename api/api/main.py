"""Tag generator API based on MultiClass LR model."""

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from api.endpoints import router
from api.settings import settings

VERSION = "0.0.1"


def custom_openapi():  # type: ignore # fastapi return a generic type
    """Define the metadata for openapi (ex swagger) specification."""
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.API_NAME,
        version=VERSION,
        summary=settings.API_SUMMARY,
        description=settings.API_DESCRIPTION,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {"url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"}
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=VERSION,
)

app.include_router(router)
app.openapi = custom_openapi  # type: ignore # conflict between mypy and fastapi

if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
