# UTILITIES IMPORTS
import utilities.SessionState as SessionState
import utilities.requests_server as requests_server
from time import sleep

# MODULES IMPORTS
import streamlit as st

def run(session_state):

    if st.button("↩️ login"):
        session_state.page = "login"
        st.experimental_rerun()

    st.write("-----------")

    mail = st.text_input("e-mail:")
    password = st.text_input("password:", type="password")
    first_name = st.text_input("first name:")
    name = st.text_input("last name:")
    starting_capital = st.number_input("start capital (USD$)", value=0)
    sure_bool = st.checkbox("yes, I want to create an account")
    if st.button("sign up"):
        if sure_bool:
            requests_server.register(first_name=first_name, name=name, mail=mail, password=password, start_capital=starting_capital)
            st.success("user was created successfully!")
            sleep(1)
            session_state.page = "login"
            st.experimental_rerun()
        else:
            st.error("user creation failed")

    st.write("-----------")