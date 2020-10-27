import streamlit as st
import side_bar
import stock_analysis_page
import requests_server
import re

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def run(session_state):

    #local_css("FrontEnd/test.css")

    st.title("Stock Screener")

    selected = st.selectbox("search by name or ticker:", [""] + session_state.stock_names)

    if st.button("OK"):
        session_state.page = "stock_info"
        session_state.stock_id = re.sub(pattern=".*: ", string=selected, repl="")
        st.experimental_rerun()
    
    side_bar.run(session_state)