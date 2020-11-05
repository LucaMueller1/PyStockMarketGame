# MODULE IMPORTS
import streamlit as st

# UTILS IMPORT
import utilities.requests_server as requests_server

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def run(session_state):

    local_css("FrontEnd/css/style.css")

    st.sidebar.title("navigation")

    with st.sidebar.beta_container():

        if st.button("📈 portfolio"):
            session_state.page = "depot"
            st.experimental_rerun()

        if st.button("💸 broker"):
            session_state.page = "boerse"
            st.experimental_rerun()

        if st.button("🔎 stock screener"):
            session_state.page = "stock_info"
            st.experimental_rerun()

        if st.button("⚙ settings️"):
            session_state.page = "about"
            st.experimental_rerun()

    st.sidebar.title("log out")

    if st.sidebar.button("bye 👋"):
        requests_server.logout(session_state.auth_key)
        session_state.page = "login"
        st.experimental_rerun()