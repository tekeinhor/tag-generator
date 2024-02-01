from typing import List

import numpy as np
import pytest
from taggenerator.preprocessing import count, detect_extension, extract_tags, filter_tag, sanitize

top_10_tags = [
    "javascript",
    "python",
    "c#",
    "java",
    "php",
    "android",
    "html",
    "jquery",
    "sql",
    "css",
]


@pytest.mark.parametrize(
    "tags, top_k_tags, expected",
    [
        (
            ["c#", "floating-point", "type-conversion", "double", "decimal"],
            top_10_tags,
            ["c#"],
        ),
        ([], top_10_tags, []),
    ],
)
def test_filter_tag(tags: List[str], top_k_tags: List[str], expected: List[str]) -> None:
    """Test filter_tag method."""
    actual = filter_tag(tags, top_k_tags)
    assert len(expected) == len(actual)


@pytest.mark.parametrize(
    "input_list, expected",
    [
        (["c#", "floating-point", "type-conversion", "double", "decimal"], 5),
        ([], 0),
        (None, 0),
    ],
    ids=["normal", "empty", "None"],
)
def test_count(input_list, expected):
    actual = count(input_list)
    assert actual == expected


@pytest.mark.parametrize(
    "input_tags, expected",
    [
        (
            "<c#>,<floating-point>,<type-conversion>,<double>,<decimal>",
            ["c#", "floating-point", "type-conversion", "double", "decimal"],
        ),
        (None, None),
        ("", []),
    ],
    ids=["normal", "None", "empty_string"],
)
def test_extract_tags(input_tags, expected):
    actual = extract_tags(input_tags)
    assert actual == expected


@pytest.mark.parametrize(
    "input_tags",
    [
        (np.NAN),
    ],
    ids=["NAN"],
)
def test_extract_tags_error(input_tags):
    with pytest.raises(TypeError) as _:
        extract_tags(input_tags)


@pytest.mark.parametrize(
    "text, expected",
    [("toto.py", True), ("toto.java", True), ("tata.xml", True), ("toto", False), (np.NAN, False), (None, False)],
)
def test_detect_extension(text, expected):
    actual = detect_extension(text)
    assert actual == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            """<p>I have an absolutely positioned <code>div</code> containing several children, one of which is a relatively positioned <code>div</code></p>""",
            """I have an absolutely positioned  containing several children, one of which is a relatively positioned""",
        ),
        (
            """<code>div</code>""",
            """""",
        ),
        (
            """I have an absolutely positioned containing several children, one of which is a relatively positioned""",
            """I have an absolutely positioned containing several children, one of which is a relatively positioned""",
        ),
    ],
    ids=["with_html_tags", "only_html_tags", "without_html_tags"],
)
def test_sanitize(text, expected):
    actual = sanitize(text)
    print(actual)
    assert actual == expected


# df = pd.DataFrame({'Tags_list': [["c#", ".net", "datetime"], ["html", "css", "internet-explorer-7"]]})
# @pytest.mark.parametrize(
#         "data, top_k_tags, expected",
#         [
#             (deepcopy(df), top_10_tags, pd.DataFrame()),
#         ]
# )
# def test_apply_filter_tag(data, top_k_tags, expected):
#     data[].apply(filter_tag)
