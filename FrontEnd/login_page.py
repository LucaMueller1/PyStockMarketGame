import streamlit as st
import SessionState
import requests
import requests_server


def run(session_state):
    user_name_input = st.text_input("user name:")
    password_input = st.text_input("password:", type="password")

    if st.button("login"):
        #session_state.page = "depot"
        #st.experimental_rerun()
        response = requests_server.login(user_name_input, password_input)

        if "authKey" in response.json():
            session_state.auth_key = response.json()["authKey"]
            response = requests_server.get_stock_names(session_state.auth_key).json()
            session_state.stock_names = [f"""{stock_dict["stockName"]}: {stock_dict["symbol"]}""" for stock_dict in response]

            session_state.page = "depot"
            st.experimental_rerun()
        else:
            st.write("username and/or password were not found.")