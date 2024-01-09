"""Contains API requests schemas definitions."""
from typing import List

from pydantic import BaseModel
from tag_generator.inference_pipeline import ModelMetada


class PredictionInput(BaseModel):  # type: ignore # incompatibility between pydantic and mypy v1.8
    """API prediction input payload schema."""

    title: str
    body: str


class PredictionOutput(BaseModel):  # type: ignore # incompatibility between pydantic and mypy v1.8
    """API prediction output payload schema."""

    ml_model_metadata: ModelMetada
    tags: List[str]
