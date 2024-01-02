"""Admin page for monitoring."""
from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

print(Path(__file__).resolve())
current_file = Path(__file__)
config_file = current_file.parents[1] / "config/users.yaml"

st.write("# Admin Dashboard! 👋")


with open(str(config_file), encoding="utf-8") as file:
    config = yaml.load(file, Loader=SafeLoader)


authenticator = stauth.Authenticate(
    config["credentials"], config["cookie"]["name"], config["cookie"]["key"], config["cookie"]["expiry_days"]
)

authenticator.login("Login", "main")

if st.session_state["authentication_status"]:
    authenticator.logout("Logout", "main", key="unique_key")
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title("Some content")
elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
