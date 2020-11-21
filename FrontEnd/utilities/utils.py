"""
    desc:       general utils module for PyBroker Streamlit GUI
    author:     Ben Schaper
    date:       2020-11-09
"""
# MODULE IMPORTS
import streamlit as st

def local_css(file_path: str) -> None:
        """
        desc:   enables Streamlit to use custom css.
        param:  (str) file_path
        test:   pass: proper file_path is provided. CSS is loaded.
                fail: file path is corrupt.
        source: https://discuss.streamlit.io/t/are-you-using-html-in-markdown-tell-us-why/96/25
        """
        with open(file_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)