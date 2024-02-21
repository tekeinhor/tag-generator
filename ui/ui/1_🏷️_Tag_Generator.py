"""UI for tag generator."""
import json
from http import HTTPStatus
from pathlib import Path
from typing import List

import requests
import streamlit as st
from tools.logger import set_logger

from ui.settings import settings

current_file = Path(__file__)
dirname = current_file.parent.stem
logger = set_logger(dirname)

st.set_page_config(
    page_title="Tag Generator",
    page_icon="🏷️",
)


def call_api(title: str, body: str) -> List[str]:
    """Call to the API for tags generation."""
    payload = {"title": title, "body": body}

    logger.info("calling API at %s with payload: %s", settings.API_ENDPOINT_URL, payload)
    response = requests.post(settings.API_ENDPOINT_URL, data=json.dumps(payload), timeout=60)
    if response.status_code == HTTPStatus.OK:
        output = json.loads(response.content)
        tags: List[str] = output["tags"]
        return tags
    return ["no-tag-found"]


with st.sidebar:
    st.write("This code will be printed to the sidebar.")

with st.container():
    st.header(":label: Tag Generator", divider="red")
    st.markdown(
        """
This is a tag generator for stackoverflow questions.
You can tap your own question, or copy paste from StackOverflow. And we will suggest tags for you.
        """
    )
    notif_cols = st.columns(1)
    with st.form("my_form"):
        title_input = st.text_input("## Title", "")
        body_text = st.text_area("## Body", "")

        submit = st.form_submit_button(
            "Predict",
            type="primary",
            help="Click on me, for tag generation",
            use_container_width=True,
        )

    if submit:
        logger.info("the submit button has been hit")
        if title_input and body_text:
            try:
                predictions = call_api(title=title_input, body=body_text)
                logger.info("api call was successfull %s", predictions)
                nb_predictions = len(predictions)
                if nb_predictions == 0:
                    st.link_button("no-tag-found", "", type="secondary")
                else:
                    cols = st.columns(nb_predictions, gap="small")
                    nb_cols_per_rows = 4

                    for i, col in enumerate(cols):
                        # col = cols[i%nb_cols_per_rows]
                        col.link_button(predictions[i], "")

            except requests.exceptions.ConnectionError as error:
                logger.error("An error has occured: %s", error)
                notif_cols[0].error("Something went wrong on our side, please try again later.", icon="🚨")
        else:
            notif_cols[0].warning("You need to specify a title and a body!", icon="⚠️")
