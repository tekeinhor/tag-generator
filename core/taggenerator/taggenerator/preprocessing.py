"""Contains all preprocessing functions."""
import re
from collections.abc import Sized
from pathlib import Path
from typing import List

import nltk
from langdetect import detect
from lxml.html.clean import Cleaner  # pylint: disable=no-name-in-module
from nltk.stem import WordNetLemmatizer
from spacy.language import Language
from tools.logger import set_logger

current_file = Path(__file__)
dirname = current_file.parent.stem
logger = set_logger(dirname)


def count(x: Sized) -> int:
    """Return len of sized element."""
    if x is not None:
        return len(x)
    return 0


def top_k(x: str, k: int = 50) -> str:
    """Return first k elements of string."""
    return x[0:k]


def extract_tags(txt: str) -> List[str]:
    """Change tags formating from '<tag1>,<tag2>' to ['tag1','tag2']."""
    if txt is None:
        return None
    p = re.compile(r"<(.*?)>")

    try:
        return p.findall(txt)
    except TypeError as type_error:
        logger.error("Following text: %s has:\n%s", txt, p)
        raise type_error


def detect_extension(text: str) -> bool:
    """Return wether an input contain a file with its extension."""
    try:
        if text:
            match = re.search(r"(.+)?\.(py|xml|java)", text)
            return match is not None
        return False
    except Exception:  # pylint: disable=broad-exception-caught, TODO
        return False


def sanitize(text: str) -> str:
    """Sanitize the input string by remove any html tags and keep only the content.

    Note: Tags and contents will be removed for <code> and <pre> tags.
    """
    # remove all tags, remove content of code and pre tags
    cleaner = Cleaner(remove_unknown_tags=False, allow_tags=[""], kill_tags=["code", "pre"])
    try:
        html_str = cleaner.clean_html(text)
    except AttributeError as _:
        return ""
    except AssertionError as _:
        # means by killing the code and pre tags, there is nothing left
        return ""
    html_str = re.sub(r"^<div>", "", html_str)
    html_str = re.sub(r"</div>$", "", html_str)
    return html_str.strip()  # type: ignore # (re pack ill-typed)


def detect_lang(x: str) -> str:
    """Detect language of input text."""
    try:
        return detect(x)  # type: ignore # generic return from external lib
    except Exception:  # pylint: disable=broad-exception-caught, TODO
        return ""


def remove_pos(x: str, language_model: Language, pos_list: List[str] | None) -> str:
    """Remove tokens that are not in pos_list."""
    if pos_list is None:
        pos_list = ["NOUN", "PROPN"]
    doc = language_model(x)
    list_text_row = []
    for token in doc:
        if token.pos_ in pos_list:
            list_text_row.append(token.text)
    join_text_row = " ".join(list_text_row)
    join_text_row = join_text_row.lower().replace("c #", "c#")
    return join_text_row


def text_cleaner(
    x: str,
    lemmatizer: WordNetLemmatizer,
    stop_words: List[str],
    language_model: Language,
) -> List[str]:
    """Apply a succession of transformations to text."""
    pos_list = ["NOUN", "PROPN"]
    # Remove POS not in "NOUN", "PROPN"
    x = remove_pos(x, language_model, pos_list)

    # Case normalization
    x = x.lower()
    # Remove unicode characters
    x = x.encode("ascii", "ignore").decode()
    # Remove links
    x = re.sub(r"http*\S+", "", x)
    # Remove numbers
    x = re.sub(r"\w*\d+\w*", "", x)
    # Remove extra spaces
    x = re.sub(r"\s+", " ", x)

    # Return cleaned text
    # Tokenization
    x = nltk.tokenize.word_tokenize(x)
    # Remove stop words
    x = [word for word in x if word not in stop_words and len(word) > 2]
    # Lemmatizer
    x = [lemmatizer.lemmatize(word) for word in x]

    # Return cleaned text
    return x


def filter_tag(x: List[str], top_list: list[str]) -> List[str]:
    """Comparison of the elements of 2 lists to check if all the tags are found in a list of top tags."""
    temp_list = []
    for item in x:
        if item in top_list:
            temp_list.append(item)
    return temp_list
