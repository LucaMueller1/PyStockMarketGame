# PAGE IMPORTS
import pages.side_bar as side_bar

# UTILITIES IMPORTS
import utilities.chart_generator as chart_generator
import utilities.requests_server as requests_server

# MODULES IMPORTS
import streamlit as st
import re
from giphypop import random_gif

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def run(session_state):

    #local_css("FrontEnd/test.css")

    st.title("stock screener")

    selected = st.selectbox("search by name or ticker:", [""] + session_state.stock_names)

    if st.button("OK"):
        gif = random_gif(tag="animal cute dog cat bear pig giraffe", api_key="AQPeA7J1SUXWSzjFPfCGd2j1nERlE81O")
        st.write("---------")
        st.markdown(f"""<img src="{gif.media_url}" style="border-radius: 1%; max-width: 50%;">""", unsafe_allow_html=True)
        st.subheader("loading information...")

        symbol = re.sub(pattern=".*: ", string=selected, repl="")
        session_state.stock_desc = requests_server.get_stock_description(session_state.auth_key, symbol)
        session_state.graph_data = requests_server.get_stockprice_history(session_state.auth_key,
                                                                          session_state.stock_desc["symbol"],
                                                                          "1y")
        session_state.page = "stock_info"
        st.experimental_rerun()


    side_bar.run(session_state)