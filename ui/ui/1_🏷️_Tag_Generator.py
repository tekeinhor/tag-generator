"""UI for tag generator."""
import json
from http import HTTPStatus
from typing import List

import requests
import streamlit as st

from settings import settings

st.set_page_config(
    page_title="Tag Generator",
    page_icon="🏷️",
)


def call_api(title: str, body: str) -> List[str]:
    """Call to the API for tags generation."""
    payload = {"title": title, "body": body}
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
        if title_input and body_text:
            predictions = call_api(title=title_input, body=body_text)
            # predictions = ("dictionary", "python", "vs-code", "py", "c#")
            nb_predictions = len(predictions)
            if nb_predictions == 0:
                st.link_button("no-tag-found", "", type="secondary")
            else:
                cols = st.columns(nb_predictions, gap="small")
                nb_cols_per_rows = 4

                for i, col in enumerate(cols):
                    # col = cols[i%nb_cols_per_rows]
                    col.link_button(predictions[i], "")
        else:
            notif_cols[0].warning("You need to specify a title and a body!", icon="⚠️")
            # st.warning("You need to specify a title and a body!", icon="⚠️")
