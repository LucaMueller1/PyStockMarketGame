import streamlit as st
import side_bar

def run(session_state):


    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    def remote_css(url):
        st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

    def icon(icon_name):
        st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

    local_css("FrontEnd/test.css")
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
    
    st.title("Stock Screener")

    icon("search")
    selected = st.text_input("search by stock name or ticker:", "")
    if st.button("OK"):
        session_state.page="depot"
        st.experimental_rerun()
