# PAGE IMPORTS
import pages.login.login_page as login_page
import pages.login.registration_page as registration_page
import pages.portfolio.depot_page as depot_page
import pages.broker.boerse_page as boerse_page
import pages.broker.boerse_page_sell as boerse_page_sell
import pages.stock_screener.stock_screener_page as stock_screener_page
import pages.stock_screener.stock_analysis_page as stock_analysis_page
import pages.about_settings.about_page as about_page

# UTILITIES IMPORTS
import utilities.requests_server as requests_server
import utilities.SessionState as SessionState

# MODULES IMPORTS
import streamlit as st


st.beta_set_page_config(page_title="PyBroker")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

session_state = SessionState.get(page='login', auth_key='', stock_desc=None, stock_names=None, first_name=None, buy_redirect=False)

if session_state.page == "login":
    login_page.run(session_state)
if session_state.page == "registration":
    registration_page.run(session_state)
if session_state.page == "depot":
    depot_page.run(session_state)
if session_state.page == "boerse":
    boerse_page.run(session_state)
if session_state.page == "stock_info" and session_state.stock_desc is not None:
    stock_analysis_page.run(session_state)
if session_state.page == "stock_info" and session_state.stock_desc is None:
    stock_screener_page.run(session_state)
# Broker page is divided into boerse and sell page, which is why it is listed as a separate session_state page below
if session_state.page == "sell":
    boerse_page_sell.run(session_state)
if session_state.page == "about":
    about_page.run(session_state)