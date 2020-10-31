# PAGE IMPORTS
import pages.side_bar as side_bar
import streamlit as st


def run(session_state):
    side_bar.run(session_state)

    st.title("About us")
    st.header("Gebühreneinstellungen:")

    # Slider for setting the transaction fee (step size = 0.5)
    transaction_fee = st.slider("Gebühren:", 1.0, 30.0, step = 0.5)