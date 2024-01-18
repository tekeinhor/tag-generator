"""API Engine definition."""
from typing import Optional

import joblib
import numpy.typing as npt
from tag_generator.inference_pipeline import InferenceEngine, ModelArtifacts, ModelMetada
from tools.logger import logger

from api.settings import settings


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
        return self.inference.predict(features)  # type: ignore # TO DO

    @staticmethod
    def load_model_from_s3() -> None:
        """Load the model from s3."""

    @staticmethod
    def load_model_from_local_fs() -> ModelArtifacts:
        """Load the model from the local file system."""
        logger.info("Starting loading the model...")
        model_dir_path = settings.LOCAL_MODEL_PATH_DIR
        model_name = "193120_final_so_questions_2008_2023_multi_lr_nlp_model.pkl"
        binarizer_name = "193120_final_so_questions_2008_2023_multilabel_binarizer.pkl"
        vertorizer_name = "193120_final_so_questions_2008_2023_tfidf_vectorizer.pkl"

        logger.info("Loading model artifacts...")
        multi_lr_cv = joblib.load(model_dir_path + "/" + model_name)
        binarizer = joblib.load(model_dir_path + "/" + binarizer_name)
        vectorizer = joblib.load(model_dir_path + "/" + vertorizer_name)
        default_metadata: ModelMetada = {
            "name": "",
            "version": 1,
            "description": "This is my model",
            "training_data": "",
        }
        return ModelArtifacts(multi_lr_cv, binarizer, vectorizer, default_metadata)
