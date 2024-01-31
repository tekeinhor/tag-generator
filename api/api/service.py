"""API Engine definition."""
from io import BytesIO
from pathlib import Path
from typing import Optional

import boto3
import joblib
import numpy.typing as npt
from tag_generator.inference_pipeline import InferenceEngine, ModelArtifacts
from tools.logger import set_logger

from api.settings import settings

current_file = Path(__file__)
dirname = current_file.parent.stem
logger = set_logger(dirname)


class Engine:
    """Engine singleton used to perform prediction in the API."""

    def __init__(self, artifacts: Optional[ModelArtifacts]):
        """Create the inference engine that will be used for prediction."""
        if artifacts is None:
            raise ValueError("Please provide a valid model artifacts object")
        self.inference = InferenceEngine(artifacts)

    def predict(self, title: str, body: str) -> npt.ArrayLike:
        """Create features and perform prediction given a title and a body."""
        features = self.inference.create_features(title, body)
        return self.inference.predict(features)

    @staticmethod
    def load_model_from_s3(bucket: str, key: str, session_profile: str) -> ModelArtifacts:
        """Load the model from s3."""
        logger.info("Starting loading the model from %s and %s", bucket, key)
        with BytesIO() as artifacts_file:
            session = boto3.Session(profile_name=session_profile)
            session.client("s3").download_fileobj(Bucket=bucket, Key=key, Fileobj=artifacts_file)
            artifacts_file.seek(0)
            artifacts = joblib.load(artifacts_file)

        return ModelArtifacts(
            artifacts["model"],
            artifacts["binarizer"],
            artifacts["vectorizer"],
            artifacts["metadata"],
        )

    @staticmethod
    def load_model_from_local_fs() -> ModelArtifacts:
        """Load the model from the local file system."""
        logger.info("Starting loading the model from file...")
        model_dir_path = settings.LOCAL_MODEL_PATH_DIR
        logger.info("Loading model artifacts...")
        artifacts = joblib.load(f"{model_dir_path}/193120_final_so_questions_2008_2023_artifacts_v1.0.0.pkl")
        return ModelArtifacts(
            artifacts["model"],
            artifacts["binarizer"],
            artifacts["vectorizer"],
            artifacts["metadata"],
        )
