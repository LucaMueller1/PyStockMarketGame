import streamlit as st

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def run(session_state):

    local_css("FrontEnd/style.css")

    st.sidebar.header("navigation")

    with st.sidebar.beta_container():

        if st.button("📈 Portfolio"):
            session_state.page = "depot"
            st.experimental_rerun()

        if st.button("💸 Börse"):
            session_state.page = "boerse"
            st.experimental_rerun()

        if st.button("🔎 Wertpapier-Suche"):
            session_state.page = "search"
            st.experimental_rerun()

    st.sidebar.header("log out")

    if st.sidebar.button("bye 👋"):
        session_state.page = "login"
        st.experimental_rerun()