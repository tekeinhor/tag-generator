import numpy as np
import pandas as pd
import pytest
from tag_generator.feature_pipeline import create_tags_pipe

simple_data = {
    "Title": [
        "Why did the width collapse in the percentage width child element in an absolutely positioned parent on Internet Explorer 7?",
        "How to convert Decimal to Double in C#?",
    ],
    "Body": ["body content", "body content"],
    "Tags": [
        "<html><css><internet-explorer-7>",
        "<c#><floating-point><type-conversion><double><decimal>",
    ],
}

data_with_na = {
    "Title": [
        "Why did the width collapse in the percentage width child element in an absolutely positioned parent on Internet Explorer 7?",
        "How to convert Decimal to Double in C#?",
        np.NAN,
    ],
    "Body": ["body content", "body content", np.NAN],
    "Tags": [
        "<html><css><internet-explorer-7>",
        "<c#><floating-point><type-conversion><double><decimal>",
        np.NAN,
    ],
}


@pytest.mark.parametrize(
    "input_data,expected_shape",
    [(simple_data, (2, 8)), (data_with_na, (2, 8))],
)
def test_create_tags_pipe(input_data, expected_shape):
    first_k = 5
    input_df = pd.DataFrame(data=input_data)
    actual_df = create_tags_pipe(input_df, first_k)
    assert actual_df.shape == expected_shape
