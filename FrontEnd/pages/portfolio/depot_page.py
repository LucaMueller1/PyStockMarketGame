"""
    desc:       portfolio module for PyBroker Streamlit GUI
    author:     Ben Schaper
    date:       2020-11-16
"""
# PAGE IMPORTS
import pages.side_bar as side_bar

# UTILITIES IMPORTS
from utilities.html_table_generator import PortfolioTable as PortfolioTable
import utilities.chart_generator as chart_generator
import utilities.requests_server as requests_server

# MODULES IMPORTS
import streamlit as st

def run(session_state):
    """
    desc:   run the log in page, requires SessionState object
            for storing session variables.
    param:  (SessionState) session_state
    """

    portfolio = requests_server.get_user_portfolio(session_state.auth_key)
    user = requests_server.get_user(session_state.auth_key)
    portfolio_history = requests_server.get_portfolio_history(session_state.auth_key)

    st.title("Portfolio")
    st.header("Hello " + user["firstName"] + ".")

    #st.header(portfolio_history[-1]["marketValue"])
    st.write("-----")

    if not "status" in portfolio_history:
        chart_generator.show_portfolio_chart(session_state.theme, portfolio_history)

    st.write("-----")
    st.subheader("Investments:")
    html_table = PortfolioTable()
    html_table.open_table()
    html_table.add_headers()
    html_table.add_portfolio(portfolio)
    html_table.close_table()

    st.markdown(html_table.get_html(), unsafe_allow_html=True)

    st.write("-----")
    st.subheader("Current portfolio value: 5000$")
    st.subheader("Available cash: " + str(user["moneyAvailable"]) + "$")

    side_bar.run(session_state)