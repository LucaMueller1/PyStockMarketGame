"""
    desc:       user registration module for PyBroker Streamlit GUI
    author:     Ben Schaper
    date:       2020-11-09
"""

# UTILITIES IMPORTS
import utilities.SessionState as SessionState
import utilities.requests_server as requests_server

# MODULES IMPORTS
import streamlit as st
from time import sleep

def run(session_state):
    """
        desc:   run the log in page, requires SessionState object
                for storing session variables.
        param:  (SessionState) session_state
    """

    if st.button("↩️ login"):
        session_state.page = "login"
        st.experimental_rerun()

    st.write("-----------")

    input_mail = st.text_input("e-mail:")
    input_password = st.text_input("password:", type="password")
    input_first_name = st.text_input("first name:")
    input_name = st.text_input("last name:")
    input_starting_capital = st.number_input("start capital (USD$)", value=0)

    sure_bool = st.checkbox("yes, I want to create an account")

    if st.button("sign up"):
        if sure_bool:
            signup_response = requests_server.register(first_name=input_first_name, name=input_name, mail=input_mail, password=input_password, start_capital=input_starting_capital)
            if(type(signup_response) == str):
                st.success("user was created successfully!")
                sleep(1)
                session_state.page = "login"
                st.experimental_rerun()
            else:
                st.error("User creation failed")
        else:
            st.error("Are you sure?")

    st.write("-----------")