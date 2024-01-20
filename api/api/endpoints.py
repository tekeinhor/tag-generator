"""Define all the endpoints of the API."""
from functools import lru_cache
from http import HTTPStatus
from pathlib import Path

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from starlette.requests import Request
from tag_generator.inference_pipeline import ModelMetada
from tools.logger import set_logger

from api.request_schemas import PredictionInput, PredictionOutput
from api.service import Engine
from api.settings import settings

current_file = Path(__file__)
dirname = current_file.parent.stem
logger = set_logger(dirname)

router = APIRouter(prefix=settings.API_PREFIX)


@lru_cache
def get_engine() -> Engine:
    """Create the Engine using lru_cache in order to not reinvoque at every router call."""
    model_artifacts = Engine.load_model_from_local_fs()
    return Engine(model_artifacts)


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
def get_models(engine: Engine = Depends(get_engine)) -> ModelMetada:
    """Return models information."""
    return engine.inference.artifacts.metadata


@router.post(
    "/predict",
    summary="Get predictions.",
    description="",
    tags=["ML"],
)
def predict(request: Request, input_data: PredictionInput, engine: Engine = Depends(get_engine)) -> PredictionOutput:
    """Perfom predictions."""
    logger.info("Call %s", request.url)
    predictions = engine.predict(input_data.title, input_data.body)
    output = PredictionOutput(
        ml_model_metadata=engine.inference.artifacts.metadata, tags=list(predictions[0])  # type: ignore # TO DO
    )
    return output
