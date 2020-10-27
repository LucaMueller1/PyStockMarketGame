import streamlit as st

def run(session_state):


    if st.sidebar.button("Depot"):
        session_state.page = "depot"
        st.experimental_rerun()

    if st.sidebar.button("Börse"):
        session_state.page = "boerse"
        st.experimental_rerun()

    if st.sidebar.button("Wertpapier-Suche"):
        session_state.page = "search"
        st.experimental_rerun()

    if st.sidebar.button("log out"):
        session_state.page = "login"
        st.experimental_rerun()