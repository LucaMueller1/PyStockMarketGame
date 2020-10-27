import streamlit as st
import side_bar

def run(session_state):

    if st.button("🔍 return to search"):
        session_state.stock_id = None
        st.experimental_rerun()

    st.header("stock analysis for")
    st.title(session_state.stock_id)
    side_bar.run(session_state)
