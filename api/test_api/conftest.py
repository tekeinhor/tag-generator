"""The conftest.py file provides fixtures for an entire directory.

Fixtures defined here can be used by any test in this package without needing to
import them (pytest will discover them).
"""
import pytest
from taggenerator.inference_pipeline import ModelArtifacts, ModelMetada

from api.service import Engine


@pytest.fixture
def default_mocked_artifacts() -> ModelArtifacts:
    return ModelArtifacts(
        None,
        None,
        None,
        {
            "name": "",
            "version": "1.0.0",
            "description": "This is my model",
            "training_data": "",
        },
    )


@pytest.fixture
def local_mocked_artifacts() -> ModelArtifacts:
    return Engine.load_model_from_local_fs()


@pytest.fixture
def default_mocked_engine() -> Engine:
    model = ModelArtifacts(
        None,
        None,
        None,
        {
            "name": "",
            "version": "1.0.0",
            "description": "This is my model",
            "training_data": "",
        },
    )
    return Engine(model)
