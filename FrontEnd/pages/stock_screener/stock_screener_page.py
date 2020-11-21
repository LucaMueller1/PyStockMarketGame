"""
    desc:       stock search module for PyBroker Streamlit GUI
    author:     Ben Schaper
    date:       2020-11-09
"""
# PAGE IMPORTS
import pages.side_bar as side_bar

# UTILITIES IMPORTS
import utilities.requests_server as requests_server
from utilities.SessionState import SessionState

# MODULES IMPORTS
import streamlit as st
import re
from giphypop import random_gif


def run(session_state: SessionState):
    """
    desc:   run the stock analysis page, requires SessionState object
            for storing session variables.
    param:  (SessionState.SessionState) session_state
    test:   pass: proper SessionState.SessionState is provided
            fail: provided SessionState.SessionState has the wrong variables
    """

    st.title("Stock Screener")

    selected = st.selectbox(
        "search by name or ticker:",
        [""] + requests_server.get_combined_stock_names(session_state.auth_key),
    )

    if st.button("OK"):
        if selected != "":
            gif = random_gif(
                tag=session_state.gif_tag[0],
                api_key="AQPeA7J1SUXWSzjFPfCGd2j1nERlE81O",
            )
            st.write("---------")
            st.markdown(
                f"""<img src="{gif.media_url}" style="border-radius: 1%; max-width: 50%;">""",
                unsafe_allow_html=True,
            )
            st.subheader("loading information...")

            symbol = re.sub(pattern=".*: ", string=selected, repl="")
            session_state.stock_desc = requests_server.get_stock_description(
                session_state.auth_key, symbol
            )
            session_state.graph_data = requests_server.get_stockprice_history(
                session_state.auth_key, session_state.stock_desc["symbol"], "max"
            )
            session_state.page = "stock_info"
            st.experimental_rerun()

    side_bar.run(session_state)
