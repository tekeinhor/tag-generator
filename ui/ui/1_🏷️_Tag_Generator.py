"""UI for tag generator."""
import streamlit as st

st.set_page_config(
    page_title="Tag Generator",
    page_icon="🏷️",
)


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
    with st.form("my_form"):
        title = st.text_input("## Title", "")
        body = st.text_area("## Body", "")

        submit = st.form_submit_button(
            "Predict", type="primary", help="Click on me, for tag generation", use_container_width=True
        )

    if submit:
        predictions = ("dictionary", "python", "vs-code", "py", "c#")
        nb_predictions = len(predictions)

        cols = st.columns(nb_predictions, gap="small")
        nb_cols_per_rows = 4

        for i, col in enumerate(cols):
            # col = cols[i%nb_cols_per_rows]
            col.link_button(predictions[i], "")
