"""
    desc:       log in module for PyBroker Streamlit GUI
    author:     Ben Schaper
    date:       2020-11-09
"""

# UTILITIES IMPORTS
import utilities.SessionState as SessionState
import utilities.requests_server as requests_server

# MODULE IMPORTS
import streamlit as st


def run(session_state):
    """
    desc:   run the log in page, requires SessionState object
            for storing session variables.
    param:  (SessionState) session_state
    """
    
    st.write(session_state.auth_key)

    if st.button("↪️ signup"):
        session_state.page = "registration"
        st.experimental_rerun()

    st.write("-----------")

    user_name_input = st.text_input("e-mail:")
    password_input = st.text_input("password:", type="password")

    if st.button("log in"):

        login_response = requests_server.login(user_name_input, password_input)

        if "authKey" in login_response:
            session_state.auth_key = login_response["authKey"]

            session_state.page = "depot"
            st.experimental_rerun()
        else:
            st.error("Incorrect user name or password.")

    st.write("-----------")
