import login_page
import depot_page
import SessionState
import boerse_page
import streamlit as st



session_state = SessionState.get(page='login', auth_key='')

if session_state.page == "login":
    login_page.run(session_state)
if session_state.page == "depot":
    depot_page.run(session_state)
if session_state.page == "boerse":
    boerse_page.run(session_state)

