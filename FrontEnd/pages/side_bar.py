# MODULE IMPORTS
import streamlit as st

# UTILS IMPORT
import utilities.requests_server as requests_server
import utilities.utils as utils
import utilities.SessionState as SessionState

def run(session_state):

    #utils.local_css("FrontEnd/css/style.css")

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

    st.sidebar.title("Theme")

    if session_state.theme == "dark":
        if st.sidebar.button("🌝"):
            session_state.theme = "light"
            st.experimental_rerun()

    if session_state.theme == "light":
        if st.sidebar.button("🌚"):
            session_state.theme = "dark"
            st.experimental_rerun()

    st.sidebar.subheader("Log Out")

    if st.sidebar.button("Bye 👋"):
        requests_server.logout(session_state.auth_key)

        session_state.auth_key=''
        session_state.stock_desc=None
        session_state.graph_data=None
        session_state.buy_redirect=False
        session_state.gif_tag=("AustinPowers", 0)
        session_state.theme = "light"
        session_state.page = "login"

        st.experimental_rerun()