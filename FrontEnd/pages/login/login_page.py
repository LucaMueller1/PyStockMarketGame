# UTILITIES IMPORTS
import utilities.SessionState as SessionState
import utilities.requests_server as requests_server

# MODULE IMPORTS
import streamlit as st


def run(session_state):
    """
    4000100 run login page
    """

    if st.button("↪️ signup"):
        session_state.page = "registration"
        st.experimental_rerun()

    st.write("-----------")

    user_name_input = st.text_input("e-mail:")
    password_input = st.text_input("password:", type="password")

    if st.button("log in"):
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
            st.warning("you entered invalid credentials")

    st.write("-----------")