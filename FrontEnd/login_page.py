import streamlit as st
import SessionState
import requests


def run(session_state):
    user_name_input = st.text_input("user name:")
    password_input = st.text_input("password:", type="password")

    if st.button("login"):
        session_state.page = "depot"
        st.experimental_rerun()
        response = login_request(user_name_input, password_input)
        if "authKey" in response.json():
            session_state.auth_key = response.json()["authKey"]
            session_state.page = "depot"
            st.experimental_rerun()
        else:
            st.write("username and/or password were not found.")

def login_request(user_name_input: str, password_input: str) -> requests.Response:
    url = "http://localhost:8080/api/user/login"
    json = {'email': user_name_input,
            'password': password_input}

    return requests.post(url, json=json)


