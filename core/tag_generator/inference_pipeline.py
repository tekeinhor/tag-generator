"""Pipeline for performing prediction."""
import joblib
import nltk
import spacy
from nltk.corpus import stopwords
from tag_generator.feature_pipeline import test_input_data
from tools.logger import logger

if __name__ == "__main__":
    logger.info("Starting inference...")
    model_dir_path = "/Users/tatia/Developer/tag-generator/artifacts/2023-12-23/18/data/"
    model_name = "185202_clean_so_questions_2008_2023_multi_lr_model.pkl"
    binarizer_name = "185202_clean_so_questions_2008_2023_multilabel_binarizer.pkl"
    vertorizer_name = "185202_clean_so_questions_2008_2023_tfidf_vectorizer.pkl"

    logger.info("Loading model artifacts...")
    multi_lr_cv = joblib.load(model_dir_path + model_name)
    binarizer = joblib.load(model_dir_path + binarizer_name)
    vectorizer = joblib.load(model_dir_path + vertorizer_name)

    k = 50
    # setting up spacy and nltk
    english_model = spacy.load("en_core_web_sm", exclude=["tok2vec", "ner", "parser", "lemmatizer"])
    lang = "english"
    stop_words = stopwords.words(lang)
    wordnet_lemmatizer = nltk.WordNetLemmatizer()
    # create ruler to transform
    ruler = english_model.get_pipe("attribute_ruler")
    pattern = [[{"TEXT": {"REGEX": r"^(.+)?\.(py|xml|java)$"}}]]
    attrs = {"POS": "PROPN"}
    # Add rules to the attribute ruler
    ruler.add(patterns=pattern, attrs=attrs, index=0)

    logger.info("Creating features...")
    _, clean_selected_col_df = test_input_data(
        "update nested dictionary in python",
        """<p>I've below dictionary</p>\
<pre class="lang-py s-code-block"><code class="hljs language-python">artistVrbl= <span class="hljs-string">'jon'</span>\
songVrbl = <span class="hljs-string">'sunshine'</span>\
dct = {<span class="hljs-string">"Artist"</span>: {<span class="hljs-string">"S"</span>:\
<span class="hljs-string">"artistVrbl"</span>},\
<span class="hljs-string">"SongTitle"</span>:\
{<span class="hljs-string">"S"</span>:<span class="hljs-string">"songVrbl"</span>}}</code></pre>\
<p>Not able to figure out to update variables value in above dictionary.</p>\
<p>expected output</p>\
<pre class="lang-py s-code-block"><code class="hljs language-python">dct = {<span class="hljs-string">"Artist"</span>:\
{<span class="hljs-string">"S"</span>: <span class="hljs-string">"jon"</span>},\
<span class="hljs-string">"SongTitle"</span>:\
{<span class="hljs-string">"S"</span>: <span class="hljs-string">"sunshine"</span>}}\
</code></pre> <p>Can anyone please suggest ?</p>""",
        wordnet_lemmatizer,
        stop_words,
        english_model,
    )
    clean_selected_col_df["Full_doc"] = clean_selected_col_df["Title"] + clean_selected_col_df["Body"]
    X = clean_selected_col_df["Full_doc"]

    print(X)

    X_tfidf = vectorizer.transform(X)

    logger.info("Perform predictions...")
    y_test_predicted_labels_tfidf = multi_lr_cv.predict(X_tfidf)

    y_test_pred_inversed = binarizer.inverse_transform(y_test_predicted_labels_tfidf)
    print(y_test_pred_inversed)
