"""
    desc:       stock analysis module for PyBroker Streamlit GUI
    author:     Ben Schaper
    date:       2020-11-09
"""
# PAGE IMPORTS
import pages.side_bar as side_bar

# UTILITIES IMPORTS
import utilities.chart_generator as chart_generator
import utilities.requests_server as requests_server
import utilities.utils as utils
import pages.broker.helperfunctions as helperfunctions
from utilities.SessionState import SessionState

# MODULES IMPORTS
import streamlit as st


def run(session_state: SessionState) -> None:
    """
    desc:   run the stock analysis page, requires SessionState object
            for storing session variables.
    param:  (SessionState.SessionState) session_state
    test:   pass: proper SessionState.SessionState is provided
            fail: provided SessionState.SessionState has the wrong variables
    """

    if st.button("🔍 return to search"):
        session_state.stock_desc = None
        st.experimental_rerun()

    sustainibility_warnings = helperfunctions.get_sustainability_info(
        session_state.auth_key, session_state.stock_desc["symbol"]
    )
    description = session_state.stock_desc

    st.markdown(
        f"""<div id="stock-title-div"><h2><img id="stock-logo" src="{description["logoUrl"]}"> {description["stockName"]}</h2></div>""",
        unsafe_allow_html=True,
    )

    chart_generator.show_stock_chart(
        session_state.theme, session_state.graph_data, description["stockName"]
    )

    show_general_info(description)
    show_financial_info(description)
    show_sustainability_warnings(description, sustainibility_warnings)

    long_description = st.beta_expander(
        f"""Description for {description["stockName"]}"""
    )
    long_description.write(f"""'{description["longDescription"]}'""")

    if st.button("🛍️ go to broker"):
        session_state.page = "boerse"
        st.experimental_rerun()

    side_bar.run(session_state)


def show_general_info(description: dict) -> None:
    general_information = st.beta_expander("General Information", expanded=True)
    general_information.write(f"""**Symbol:** {description["symbol"]}""")
    general_information.write(f"""**Country:** {description["country"]}""")
    general_information.write(f"""**Industry:** {description["industry"]}""")
    if type(description["fullTimeEmployees"]) == float:
        general_information.write(
            f"""**Full Time Employees:** {description["fullTimeEmployees"]:,}"""
        )


def show_financial_info(description: dict) -> None:
    financial_information = st.beta_expander("Financial Information", expanded=True)
    if type(description["marketCap"]) is not str:
        financial_information.write(
            f"""**Market Capitalization:** {round(description["marketCap"]/1000000000,3):,}B$"""
        )
    if type(description["dividend"]) == float:
        financial_information.write(
            f"""**Dividend Yield:** {round(description["dividend"]*100,2)}%"""
        )
    financial_information.write(
        f"""**52 Week High:** {description["fiftyTwoWeekHigh"]}$"""
    )
    financial_information.write(
        f"""**52 Week Low:** {description["fiftyTwoWeekLow"]}$"""
    )


def show_sustainability_warnings(description: dict, sustainibility_warnings: list) -> None:
    warning_information = st.beta_expander(
        f"""Warnings for {description["stockName"]}""", expanded=True
    )

    if sustainibility_warnings:
        for warning in sustainibility_warnings:
            warning_information.write("⚠️  " + warning.upper())
    else:
        warning_information.write("✅  " + "No apparent warnings")
