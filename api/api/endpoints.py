from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request
from api.settings import settings

router = APIRouter(prefix=settings.API_PREFIX)


async def lifespan(app: FastAPI):
    pass


@router.get(
    "/health",
    summary="",
    tags=["OPS"],
)
def get_health_status() -> JSONResponse:
    """Return health status of the API"""
    return JSONResponse()


@router.get(
    "/models",
    summary="",
    description="",
    tags=["ML"],
)
def get_models() -> JSONResponse:
    """Return models information."""
    return JSONResponse()


@router.post(
    "/predict",
    summary="",
    description="",
    tags=["ML"],
)
def predict(request: Request, title: str, body:str) -> JSONResponse:
    """Perfom predictions."""
    return JSONResponse() 