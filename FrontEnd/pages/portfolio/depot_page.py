# PAGE IMPORTS
import pages.side_bar as side_bar

# UTILITIES IMPORTS
from utilities.html_table_generator import PortfolioTable as PortfolioTable
import utilities.chart_generator as chart_generator
import utilities.requests_server as requests_server

# MODULES IMPORTS
import streamlit as st

def run(session_state):

    portfolio = requests_server.get_user_portfolio(session_state.auth_key)
    user = requests_server.get_user(session_state.auth_key)
    st.title("portfolio")
    st.header("Hello " + user["firstName"] + "!")
    st.subheader("Cash available: " + str(user["moneyAvailable"]) + "$")

    #chart_generator.show_chart(session_state.graph_data)

    html_table = PortfolioTable()
    html_table.open()
    html_table.add_headers()
    html_table.add_portfolio(portfolio)
    html_table.close()

    st.markdown(html_table.get_html(), unsafe_allow_html=True)

    side_bar.run(session_state)