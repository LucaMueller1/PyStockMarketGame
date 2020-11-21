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
from email_validator import validate_email, EmailNotValidError


def run(session_state):
    """
    desc:   run the registration page, requires SessionState object
            for storing session variables.
    param:  (SessionState.SessionState) session_state
    test:   pass: proper SessionState.SessionState is provided
            fail: provided SessionState.SessionState has the wrong variables
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

    st.warning("All fields are mandatory")

    sure_bool = st.checkbox("yes, I want to create an account")

    if st.button("sign up"):
        if sure_bool and input_password and input_first_name and input_name:
            try:
                validate_email(input_mail)
                signup_response = requests_server.register(
                    first_name=input_first_name,
                    name=input_name,
                    mail=input_mail,
                    password=input_password,
                    start_capital=input_starting_capital,
                )

                if type(signup_response) == str:
                    st.success("User was created successfully!")
                    st.balloons()
                    sleep(1)
                    session_state.page = "login"
                    st.experimental_rerun()
                else:
                    st.error("User creation failed")
            except EmailNotValidError as error_message:
                st.error(str(error_message))
        else:
            st.error("Missing required input")

    st.write("-----------")
