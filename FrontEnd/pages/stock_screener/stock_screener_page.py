# PAGE IMPORTS
import pages.side_bar as side_bar

# UTILITIES IMPORTS
import utilities.chart_generator as chart_generator
import utilities.requests_server as requests_server

# MODULES IMPORTS
import streamlit as st
import re

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def run(session_state):

    #local_css("FrontEnd/test.css")

    st.title("stock screener")

    selected = st.selectbox("search by name or ticker:", [""] + session_state.stock_names)

    if st.button("OK"):
        session_state.page = "stock_info"
        session_state.stock_id = re.sub(pattern=".*: ", string=selected, repl="")
        st.experimental_rerun()


    side_bar.run(session_state)