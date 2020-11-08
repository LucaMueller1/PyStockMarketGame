# MODULE IMPORTS
import streamlit as st

# UTILS IMPORT
import utilities.requests_server as requests_server
import utilities.utils as utils

def run(session_state):

    utils.local_css("FrontEnd/css/style.css")

    st.sidebar.title("Navigation")

    with st.sidebar.beta_container():

        if st.button("📈 Portfolio"):
            session_state.page = "depot"
            st.experimental_rerun()

        if st.button("💸 Broker"):
            session_state.page = "boerse"
            st.experimental_rerun()

        if st.button("🔎 Stock Screener"):
            session_state.page = "stock_info"
            st.experimental_rerun()

        if st.button("⚙ Settings️"):
            session_state.page = "about"
            st.experimental_rerun()

    st.sidebar.title("Log Out")

    if st.sidebar.button("Bye 👋"):
        requests_server.logout(session_state.auth_key)
        session_state = SessionState.get(page='login', auth_key='', stock_desc=None, stock_names=None, graph_data=None, buy_redirect=False)
        session_state.page = "login"
        st.experimental_rerun()