import login_page
import depot_page
import boerse_page
import stock_screener_page
import stock_analysis_page

import requests_server

import streamlit as st

import SessionState

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

session_state = SessionState.get(page='login', auth_key='', stock_id=None, stock_names=None)

if session_state.page == "login":
    login_page.run(session_state)
if session_state.page == "depot":
    depot_page.run(session_state)
if session_state.page == "boerse":
    boerse_page.run(session_state)
if session_state.page == "stock_info" and session_state.stock_id is not None:
    stock_analysis_page.run(session_state)
if session_state.page == "stock_info" and session_state.stock_id is None:
    stock_screener_page.run(session_state)