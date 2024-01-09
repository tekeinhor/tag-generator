"""Pipeline for features creation."""
import time
from datetime import datetime
from functools import wraps
from pathlib import Path
from typing import Callable, List, ParamSpec, Tuple, TypeVar

import nltk
import pandas as pd
import spacy
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from spacy.language import Language
from tag_generator.preprocessing import count, detect_lang, extract_tags, filter_tag, sanitize, text_cleaner, top_k
# from tag_generator.tag_generator.preprocessing import (contains_code, count, detect_extension, detect_lang,
#    extract_tags, filter_tag, sanitize, text_cleaner, top_k)
from tools.logger import logger
from tqdm.auto import tqdm

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

T = TypeVar("T")
P = ParamSpec("P")


def timeit(func: Callable[P, T]) -> Callable[P, T]:
    """Will be used a decorator for function time measurement."""

    @wraps(func)
    def timeit_wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__}, Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


@timeit
def create_tags_pipe(data_df: pd.DataFrame, first_k: int) -> pd.DataFrame:
    """Pipe for clean tags."""
    data_df = data_df[data_df["Tags"].notna()]
    logger.info("Removed line where 'Tags' is Nan %s", data_df.shape)

    data_df["Tags_list"] = data_df["Tags"].progress_apply(extract_tags)
    data_df["Tags_count"] = data_df["Tags_list"].progress_apply(count)
    logger.info("Transformed Tags into Tags List: %s", data_df.shape)

    logger.info("Dropping rows where there are no Tags...")
    tags = data_df.Tags_list.explode().value_counts().to_frame().reset_index()

    print(tags)
    data_df = data_df.drop(data_df[data_df.Tags_count == 0].index).reset_index()
    logger.info("Dropping rows where there are no Tags: %s", data_df.shape)

    logger.info("Dropping rows where there are no tags between top tags...")

    top_tags = list(tags.Tags_list.iloc[0:first_k])
    data_df["top_tags"] = data_df["Tags_list"].apply(lambda x: filter_tag(x, top_tags))
    data_df["top_tags_count"] = data_df["top_tags"].progress_apply(count)
    data_df = data_df[data_df.top_tags_count > 0]
    logger.info("Dropped rows where there are no Tags: %s", data_df.shape)

    return data_df


@timeit
def create_text_pipe(
    data_df: pd.DataFrame,
    lemmatizer: WordNetLemmatizer,
    stop_words: List[str],
    language_model: Language,
) -> pd.DataFrame:
    """Pipe for clean title and body."""
    tqdm.pandas()
    logger.info("Dropping rows where there are no Bodys...")
    data_df = data_df[data_df["Body"].notna()]
    logger.info("Dropped rows where there are no Bodys: %s", data_df.shape)

    # logger.info("Checking file extension...")
    # data_df[:,"has_ext"] = data_df["Body"].progress_apply(detect_extension)
    # data_df["contains_code"] = data_df["Body"].progress_apply(contains_code)
    # data_df[:,"contains_code"] = data_df["contains_code"].astype(int)
    # logger.info("Checked")

    logger.info("Detecting lang...")
    data_df["body_without_tags"] = data_df["Body"].progress_apply(sanitize)
    data_df = data_df[data_df["body_without_tags"].notna()]
    data_df["short_body"] = data_df["body_without_tags"].progress_apply(top_k)
    data_df["lang"] = data_df.short_body.progress_apply(detect_lang)
    data_df = data_df[data_df["lang"] == "en"]
    logger.info("Keeping english content: %s", data_df.shape)

    logger.info("Cleaning body...")
    data_df["clean_body"] = data_df.body_without_tags.progress_apply(
        lambda x: text_cleaner(
            x,
            lemmatizer=lemmatizer,
            stop_words=stop_words,
            language_model=language_model,
        )
    )
    data_df["body_tokens_count"] = [len(_) for _ in data_df.clean_body]
    logger.info("Cleaned body: %s", data_df.shape)

    logger.info("Cleaning title...")
    data_df["clean_title"] = data_df.Title.progress_apply(
        lambda x: text_cleaner(
            x,
            lemmatizer=lemmatizer,
            stop_words=stop_words,
            language_model=language_model,
        )
    )
    data_df["title_tokens_count"] = [len(_) for _ in data_df.clean_title]
    logger.info("Cleaned title: %s", data_df.shape)

    return data_df


@timeit
def create_pipe(
    data_df: pd.DataFrame,
    first_k: int,
    lemmatizer: WordNetLemmatizer,
    stop_words: List[str],
    language_model: Language,
) -> pd.DataFrame:
    """Pipe to clean all relevant text."""
    tqdm.pandas()

    logger.info("Loaded data: %s", data_df.shape)

    logger.info("Cleaning Tags info..")
    data_df = create_tags_pipe(data_df, first_k)
    logger.info("Cleaned Tags info! %s", data_df.shape)

    logger.info("Cleaning Text...")
    data_df = create_text_pipe(
        data_df,
        lemmatizer=lemmatizer,
        stop_words=stop_words,
        language_model=language_model,
    )
    logger.info("Cleaned Text: %s", data_df.shape)

    # Delete items with number of Body tokens < 5
    data_df = data_df[(data_df.body_tokens_count >= 5) & (data_df.title_tokens_count > 0)]

    return data_df


def test_sample_data(
    data_file_path: str,
    first_k: int,
    lemmatizer: WordNetLemmatizer,
    stop_words: List[str],
    language_model: Language,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Used to test on sample data."""
    data_df = pd.read_csv(data_file_path)
    clean_df = create_pipe(data_df, first_k, lemmatizer, stop_words, language_model)

    selected_col = ["clean_title", "clean_body", "Score", "contains_code", "Tags_list"]
    col_new_names = {
        "clean_title": "Title",
        "clean_body": "Body",
        "contains_code": "Contains_Code",
        "top_tags": "Tags",
    }

    clean_selected_col_df = clean_df[selected_col]
    clean_selected_col_df = clean_selected_col_df.rename(columns=col_new_names)

    return clean_df, clean_selected_col_df


def test_input_data(
    title: str,
    body: str,
    lemmatizer: WordNetLemmatizer,
    stop_words: List[str],
    language_model: Language,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Test on example title and body."""
    data_df = pd.DataFrame({"Title": [title], "Body": [body]})

    clean_df = create_text_pipe(data_df, lemmatizer, stop_words, language_model)

    selected_col = ["clean_title", "clean_body", "contains_code"]
    col_new_names = {
        "clean_title": "Title",
        "clean_body": "Body",
        "contains_code": "Contains_Code",
    }

    clean_selected_col_df = clean_df[selected_col]
    clean_selected_col_df = clean_selected_col_df.rename(columns=col_new_names)

    return clean_df, clean_selected_col_df


if __name__ == "__main__":
    logger.info("Starting preprocessing...")

    k = 50

    # setting up spacy and nltk
    english_model = spacy.load("en_core_web_sm", exclude=["tok2vec", "ner", "parser", "lemmatizer"])
    lang = "english"
    englis_stop_words = stopwords.words(lang)
    wordnet_lemmatizer = nltk.WordNetLemmatizer()
    # create ruler to transform
    ruler = english_model.get_pipe("attribute_ruler")
    pattern = [[{"TEXT": {"REGEX": r"^(.+)?\.(py|xml|java)$"}}]]
    attrs = {"POS": "PROPN"}
    # Add rules to the attribute ruler
    ruler.add(patterns=pattern, attrs=attrs, index=0)  # type: ignore # external lib

    # clean_df, clean_selected_col_df = test_sample_data(
    #     "/Users/tatia/Developer/tag-generator/core/test_tag_generator/samples.csv",
    #     first_k,
    #     wordnet_lemmatizer,
    #     stop_words,
    #     english_model,
    # )

    df1, df2 = test_input_data(
        "make tqdm bar dark in VSCode Jupyter notebook",
        "I am using Jupyter notebooks in Visual Studio Code with dark mode enabled.\
        I visualize progress bars with tqdm, but it does not show up dark.\
        See the image:According to this issue on GitHub, this is not a problem with the Jupyter,\
        ipywidget or tqdm itself, and it is related only to VSCode.\
        Is there any workaround to fix this?",
        wordnet_lemmatizer,
        englis_stop_words,
        english_model,
    )

    today = datetime.now()
    time_str = today.strftime("%H%M%S")
    prefix = "/Users/tatia/Developer/tag-generator/artifacts"
    output_dir = f"{prefix}/{today.strftime('%Y-%m-%d/%H/data')}"
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    df2.to_csv(f"{output_dir}/{time_str}_clean_so_questions_2008_2023.csv")
    df1.to_csv(f"{output_dir}/{time_str}_clean_all_columns_so_questions_2008_2023.csv")

    logger.info("Final selected col: %s all: %s", df2.shape, df1.shape)
