# PAGE IMPORTS
import pages.side_bar as side_bar

# UTILITIES IMPORTS
import utilities.chart_generator as chart_generator

# MODULES IMPORTS
import streamlit as st


def run(session_state):

    if st.button("🔍 return to search"):
        session_state.stock_id = None
        st.experimental_rerun()

    st.header("stock analysis for")
    st.title(session_state.stock_id)

    chart_generator.show_chart()

    side_bar.run(session_state)
