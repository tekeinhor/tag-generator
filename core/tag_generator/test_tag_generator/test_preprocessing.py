import pytest
import pandas as pd
from copy import deepcopy
from tag_generator.tag_generator.preprocessing import filter_tag

top_10_tags = ['javascript', 'python', 'c#', 'java', 'php', 'android', 'html', 'jquery', 'sql', 'css']

@pytest.mark.parametrize(
        "tags, top_k_tags, expected",
        [
            (['c#', 'floating-point', 'type-conversion', 'double', 'decimal'], top_10_tags, ['c#']),
            ([], top_10_tags, []),
            ]

)
def test_filter_tag(tags, top_k_tags, expected):
    actual = filter_tag(tags, top_k_tags)
    assert len(expected) ==  len(actual)


# df = pd.DataFrame({'Tags_list': [["c#", ".net", "datetime"], ["html", "css", "internet-explorer-7"]]})
# @pytest.mark.parametrize(
#         "data, top_k_tags, expected",
#         [
#             (deepcopy(df), top_10_tags, pd.DataFrame()),
#         ]
# )
# def test_apply_filter_tag(data, top_k_tags, expected):
#     data[].apply(filter_tag)