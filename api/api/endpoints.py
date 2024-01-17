"""Define all the endpoints of the API."""
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from http import HTTPStatus

from fastapi import APIRouter, Depends, FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request
from tag_generator.inference_pipeline import ModelMetada
from tools.logger import logger

from api.request_schemas import PredictionInput, PredictionOutput
from api.service import Engine
from api.settings import settings

router = APIRouter(prefix=settings.API_PREFIX)
MODEL = Engine.load_model_from_local_fs()
engine = Engine(MODEL)


@router.get(
    "/health",
    summary="Get health status.",
    tags=["OPS"],
)
def get_health_status() -> JSONResponse:
    """Return health status of the API."""
    return JSONResponse(status_code=HTTPStatus.OK, content="Service healthy!")


@router.get(
    "/models",
    summary="Get models info.",
    description="",
    tags=["ML"],
)
def get_models() -> ModelMetada:
    """Return models information."""
    return engine.inference.artifacts.metadata


@router.post(
    "/predict",
    summary="Get predictions.",
    description="",
    tags=["ML"],
)
def predict(request: Request, input_data: PredictionInput) -> PredictionOutput:
    """Perfom predictions."""
    logger.info("Call %s", request.url)
    predictions = engine.predict(input_data.title, input_data.body)
    output = PredictionOutput(
        ml_model_metadata=engine.inference.artifacts.metadata, tags=list(predictions[0])  # type: ignore # TO DO
    )
    return output
