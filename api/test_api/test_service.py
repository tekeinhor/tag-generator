from unittest.mock import patch, Mock, call
import pytest
from api.service import Engine
from tag_generator.inference_pipeline import ModelArtifacts

model_dir_path = "/Users/tatia/Developer/tag-generator/core/models/2024-01-02/19"
model_name = "193120_final_so_questions_2008_2023_multi_lr_nlp_model.pkl"
binarizer_name = "193120_final_so_questions_2008_2023_multilabel_binarizer.pkl"
vertorizer_name = "193120_final_so_questions_2008_2023_tfidf_vectorizer.pkl"

path_model = f"{model_dir_path}/{model_name}"
path_bin = f"{model_dir_path}/{binarizer_name}"
path_vec = f"{model_dir_path}/{vertorizer_name}"

@patch("joblib.load")
def test_load_model_from_local_fs(mocked_joblib_load):
    """Test that the load_model_from_local_fs() raised and Exception there are no files."""
    actual = Engine.load_model_from_local_fs()

    # list call that should be made (joblib.load with different args)
    calls = [call.load(path_model), call.load(path_bin), call.load(path_vec)]
    mocked_joblib_load.assert_has_calls(calls, any_order=True)

    assert  "name" in actual.metadata


@patch("joblib.load", scope="function")
def test_load_model_from_local_fs_error(mocked_joblib_load):
    mocked_joblib_load.side_effect = [FileNotFoundError(),  FileNotFoundError(),  FileNotFoundError()]
    
    with pytest.raises(FileNotFoundError) as _: 
        Engine.load_model_from_local_fs()


def test_Engine_predict(local_mocked_artifacts: ModelArtifacts):
    engine = Engine(local_mocked_artifacts)
    actual = engine.predict("update nested dictionary in python",
                   "<p>I've below dictionary</p># <pre class=\"lang-py s-code-block\"><code class=\"hljs language-python\">artistVrbl= <span lass=\"hljs-string\">'jon'</span># songVrbl = <span class=\"hljs-string\">'sunshine'</span># dct = {<span class=\"hljs-string\">\"Artist\"</span>: {<span class=\"hljs-string\">\"S\"</span>:# <span class=\"hljs-string\">\"artistVrbl\"</span>},# <span class=\"hljs-string\">\"SongTitle\"</span>:# {<span class=\"hljs-string\">\"S\"</span>:<span class=\"hljs-string\">\"songVrbl\"</span>}}</code></pre># <p>Not able to figure out to update variables value in above dictionary.</p># <p>expected output</p># <pre class=\"lang-py s-code-block\"><code class=\"hljs language-python\">dct = {<span class=\"hljs-string\">\"Artist\"</pan>:# {<span class=\"hljs-string\">\"S\"</span>: <span class=\"hljs-string\">\"jon\"</span>},# <span class=\"hljs-string\">\"SongTitle\"</span>:# {<span class=\"hljs-string\">\"S\"</span>: <span class=\"hljs-string\">\"sunshine\"</span>}}# </code></pre> <p>Can anyone please suggest ?</p>")

    assert len(actual) == 1

def test_Engine_init():
    with pytest.raises(ValueError):
        _ = Engine(None)