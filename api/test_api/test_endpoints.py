from http import HTTPStatus
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from tag_generator.inference_pipeline import ModelArtifacts

from api.main import app
from api.service import Engine
from api.settings import settings


@pytest.fixture()
def client():
    """Create the API client that will used for test."""
    return TestClient(app)


def test_endpoint_get_health_status(client: TestClient):
    """Test the get_model endpoint."""

    result = client.get(f"{settings.API_PREFIX}/health")

    assert result.status_code == HTTPStatus.OK
    actual = result.content.decode("utf-8")
    assert "Service healthy!" in actual


@patch("api.endpoints.MODEL")
def test_endpoint_get_model(mocked_artifacts, client: TestClient, default_mocked_artifacts):
    """Test the get_model endpoint."""
    mocked_artifacts.return_value = default_mocked_artifacts

    result = client.get(f"{settings.API_PREFIX}/models")
    result_json = result.json()

    assert result.status_code == HTTPStatus.OK
    assert "name" in result_json
    assert "version" in result_json
    assert "description" in result_json
    assert "training_data" in result_json


@pytest.mark.parametrize(
    "data",
    [({})],
)
@patch("api.endpoints.MODEL")
def test_endpoint_predict_invalid_input(
    mocked_artifacts: ModelArtifacts, client: TestClient, data: dict, default_mocked_artifacts
):
    """Test the prediction endpoint."""
    mocked_artifacts.return_value = default_mocked_artifacts

    result = client.post(f"{settings.API_PREFIX}/predict", json=data, headers={"content-type": "application/json"})
    result_json = result.json()

    assert result.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert result_json["detail"][0]["type"] == "missing"
    assert result_json["detail"][0]["msg"] == "Field required"


@patch("api.endpoints.MODEL")
@patch.object(Engine, "predict", return_value=[("dictionary", "python")], scope="function")
def test_endpoint_predict(mocked_engine_predict, mocked_artifacts, client: TestClient, local_mocked_artifacts):
    """Test the prediction endpoint."""
    mocked_artifacts.return_value = local_mocked_artifacts
    data = {
        "title": "update nested dictionary in python",
        "body": '<p>I\'ve below dictionary</p># <pre class="lang-py s-code-block"><code class="hljs language-python">artistVrbl= <span lass="hljs-string">\'jon\'</span># songVrbl = <span class="hljs-string">\'sunshine\'</span># dct = {<span class="hljs-string">"Artist"</span>: {<span class="hljs-string">"S"</span>:# <span class="hljs-string">"artistVrbl"</span>},# <span class="hljs-string">"SongTitle"</span>:# {<span class="hljs-string">"S"</span>:<span class="hljs-string">"songVrbl"</span>}}</code></pre># <p>Not able to figure out to update variables value in above dictionary.</p># <p>expected output</p># <pre class="lang-py s-code-block"><code class="hljs language-python">dct = {<span class="hljs-string">"Artist"</pan>:# {<span class="hljs-string">"S"</span>: <span class="hljs-string">"jon"</span>},# <span class="hljs-string">"SongTitle"</span>:# {<span class="hljs-string">"S"</span>: <span class="hljs-string">"sunshine"</span>}}# </code></pre> <p>Can anyone please suggest ?</p>',
    }
    result = client.post(f"{settings.API_PREFIX}/predict", json=data, headers={"content-type": "application/json"})
    result_json = result.json()

    assert result.status_code == HTTPStatus.OK
    assert "ml_model_metadata" in result_json
    assert "tags" in result_json
