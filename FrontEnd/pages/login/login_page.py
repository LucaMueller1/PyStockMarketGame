import streamlit as st
import SessionState
import requests
import requests_server


def run(session_state):
    """
    4000100 run login page
    """

    login_radio = st.radio("login / register", ["login", "register"])

    st.write("-----------")

    if login_radio == "login":
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

    if login_radio == "register":
        first_name = st.text_input("input first name:")
        name = st.text_input("input name:")
        mail = st.text_input("input e-mail:")
        password = st.text_input("input password:", type="password")
        st.write("-----------")
        starting_capital = st.number_input("how much USD$ do you want to start with? (start capital)", value=0)
        sure_bool = st.checkbox("yes, I'm sure that I want to create an account!")
        if st.button("register account"):
            if sure_bool:
                requests_server.register(first_name=first_name, name=name, mail=mail, password=password, start_capital=starting_capital)
                login_radio = "login"
                st.experimental_rerun()