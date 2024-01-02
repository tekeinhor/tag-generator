""" Tag generator API based on MultiClass LR model."""

import uvicorn
from fastapi import FASTAPI

from api.settings import settings


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
        contact={
            "name": settings.CONTACT_NAME,
            "email": settings.CONTACT_EMAIL,
        },
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FASTAPI(
    lifespan=endpoints.lifespan,
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version="",
)

app.include_router(endpoints.router)
app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
