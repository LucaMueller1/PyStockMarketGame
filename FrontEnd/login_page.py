import streamlit as st
import SessionState
import requests

#session_state = SessionState.get(auth_key='')

def run(session_state):
    user_name_input = st.text_input("user name:")
    password_input = st.text_input("password:", type="password")

    if st.button("login"):
        #response = login_request()
        #st.write(response.text)
        session_state.page = "depot"
        st.experimental_rerun()

def login_request():
    url = "http://localhost:8080/api/user/login"
    json = {'email': 'somevalue',
            'password':'somevalue'}

    return requests.post(url, json=json)