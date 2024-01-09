"""Pipeline for performing prediction."""
from dataclasses import dataclass
from typing import Protocol

import joblib
import nltk
import numpy.typing as npt
import pandas as pd
import spacy
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from tag_generator.feature_pipeline import create_text_pipe
from tools.logger import logger
from typing_extensions import TypedDict


class ModelMetada(TypedDict):  # pylint:disable=too-many-ancestors, TO DO
    """Represents metadata to describe and identify an ML model."""

    name: str
    version: int
    description: str
    training_data: str


class ScikitModel(Protocol):
    """Protocol for typing Scikit ModelArtifacts Estimators."""

    def fit(self, X: npt.ArrayLike, y: npt.ArrayLike, sample_weight: npt.ArrayLike) -> npt.ArrayLike:
        """Represent the fit method of a scikit model estimators.

        This function is for type hinting only.
        """

    def predict(self, X: npt.ArrayLike) -> npt.ArrayLike:
        """Represent the predict method of a scikit model estimators.

        This function is for type hinting only.
        """

    def score(self, X: npt.ArrayLike, y: npt.ArrayLike, sample_weight: npt.ArrayLike) -> npt.ArrayLike:
        """Represent the score method of a scikit model estimators.

        This function is for type hinting only.
        """


@dataclass
class ModelArtifacts:
    """Represent the different artifacts necesary to perform an inference.

    - a scikit ML Model
    - a binarizer
    - a vectorizer
    """

    scikit_model: ScikitModel
    binarizer: MultiLabelBinarizer
    vectorizer: TfidfVectorizer
    metadata: ModelMetada = {
        "name": "",
        "version": 1,
        "description": "This is my model",
        "training_data": "",
    }


class InferenceEngine:
    """Represent the Engine that will process data to produce an inference."""

    def __init__(self, artifacts: ModelArtifacts):
        """Set up the Engine with a model artifacts object."""
        self.artifacts = artifacts
        self.lang = "english"
        self.english_model = spacy.load("en_core_web_sm", exclude=["tok2vec", "ner", "parser", "lemmatizer"])
        self.english_stop_words = stopwords.words(self.lang)
        self.lemmatizer = nltk.WordNetLemmatizer()

        # Add rules to the attribute ruler
        ruler = self.english_model.get_pipe("attribute_ruler")
        pattern = [[{"TEXT": {"REGEX": r"^(.+)?\.(py|xml|java)$"}}]]
        attrs = {"POS": "PROPN"}
        ruler.add(patterns=pattern, attrs=attrs, index=0)  # type: ignore # external lib

    def create_features(self, title: str, body: str) -> pd.DataFrame:
        """Create text features given a title and a body.

        The features pipeline perfom a set of operations, from part of speach tagging,
        to lematization, passing through stopword removal.

        The result dataframe holds the cleaned title and body lists.
        """
        data_df = pd.DataFrame({"Title": [title], "Body": [body]})

        clean_df = create_text_pipe(data_df, self.lemmatizer, self.english_stop_words, self.english_model)

        selected_col = ["clean_title", "clean_body"]
        col_new_names = {
            "clean_title": "Title",
            "clean_body": "Body",
        }
        clean_selected_col_df = clean_df[selected_col]
        clean_selected_col_df = clean_selected_col_df.rename(columns=col_new_names)
        return clean_selected_col_df

    def predict(self, features_df: pd.DataFrame) -> npt.NDArray:  # type: ignore # conflict between numpy and mypy
        """Predict, based on text features, what are the most likely tags."""
        logger.info("Perform predictions...")

        features_df["Full_doc"] = features_df["Title"] + features_df["Body"]
        X = features_df["Full_doc"]
        X_tfidf = self.artifacts.vectorizer.transform(X)
        y_test_predicted_labels_tfidf = self.artifacts.scikit_model.predict(X_tfidf)

        y_test_pred_inversed = self.artifacts.binarizer.inverse_transform(y_test_predicted_labels_tfidf)
        return y_test_pred_inversed  # type: ignore # TO DO


if __name__ == "__main__":
    logger.info("Starting inference...")
    model_dir_path = "/Users/tatia/Developer/tag-generator/core/models/2024-01-02/19"
    model_name = "193120_final_so_questions_2008_2023_multi_lr_nlp_model.pkl"
    binarizer_name = "193120_final_so_questions_2008_2023_multilabel_binarizer.pkl"
    vertorizer_name = "193120_final_so_questions_2008_2023_tfidf_vectorizer.pkl"

    logger.info("Loading model artifacts...")
    multi_lr_cv = joblib.load(model_dir_path + "/" + model_name)
    binarizer = joblib.load(model_dir_path + "/" + binarizer_name)
    vectorizer = joblib.load(model_dir_path + "/" + vertorizer_name)

    my_model = ModelArtifacts(scikit_model=multi_lr_cv, binarizer=binarizer, vectorizer=vectorizer)
    engine = InferenceEngine(my_model)

    features = engine.create_features(
        "update nested dictionary in python",
        """<p>I've below dictionary</p>\
# <pre class="lang-py s-code-block"><code class="hljs language-python">artistVrbl= <span class="hljs-string">'jon'\
</span> songVrbl = <span class="hljs-string">'sunshine'</span>\
# dct = {<span class="hljs-string">"Artist"</span>: {<span class="hljs-string">"S"</span>:\
# <span class="hljs-string">"artistVrbl"</span>},\
# <span class="hljs-string">"SongTitle"</span>:\
# {<span class="hljs-string">"S"</span>:<span class="hljs-string">"songVrbl"</span>}}</code></pre>\
# <p>Not able to figure out to update variables value in above dictionary.</p>\
# <p>expected output</p>\
# <pre class="lang-py s-code-block"><code class="hljs language-python">dct =\
{<span class="hljs-string">"Artist"</span>:# {<span class="hljs-string">"S"</span>:\
<span class="hljs-string">"jon"</span>}, <span class="hljs-string">"SongTitle"</span>:\
# {<span class="hljs-string">"S"</span>: <span class="hljs-string">"sunshine"</span>}}\
# </code></pre> <p>Can anyone please suggest ?</p>""",
    )

    predictions = engine.predict(features)
    print(predictions)
