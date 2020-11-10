# PAGE IMPORTS
import pages.side_bar as side_bar

# UTILITIES IMPORTS
import utilities.chart_generator as chart_generator
import utilities.requests_server as requests_server
import utilities.utils as utils

# MODULES IMPORTS
import streamlit as st



def run(session_state):

    utils.local_css("FrontEnd/css/style.css")
    description = session_state.stock_desc

    if st.button("🔍 return to search"):
        session_state.stock_desc = None
        st.experimental_rerun()

    st.title("Stock Screener")

    st.markdown(f"""<h2 style="max-height: 3em"><img src="{description["logoUrl"]}" style="border-radius: 10%">    {description["stockName"]}<h2>""", unsafe_allow_html=True)

    chart_generator.show_chart(session_state.graph_data)

    general_information = st.beta_expander("General Information", expanded=True)
    general_information.write(f"""**Symbol:** {description["symbol"]}""")
    general_information.write(f"""**Country:** {description["country"]}""")
    general_information.write(f"""**Industry:** {description["industry"]}""")
    general_information.write(f"""**Full Time Employees:** {description["fullTimeEmployees"]:,}""")

    financial_information = st.beta_expander("Financial Information", expanded=True)
    financial_information.write(f"""**Market Capitalization:** {round(description["marketCap"]/1000000000,3):,}B$""")
    if type(description["dividend"]) == float:
        financial_information.write(f"""**Dividend Yield:** {round(description["dividend"]*100,2)}%""")
    financial_information.write(f"""**52 Week High:** {description["fiftyTwoWeekHigh"]}$""")
    financial_information.write(f"""**52 Week Low:** {description["fiftyTwoWeekLow"]}$""")

    long_description = st.beta_expander(f"""Description for {description["stockName"]}""")
    long_description.write(f"""'{description["longDescription"]}'""")

    if st.button("🛍️ go to broker"):
        session_state.page = "boerse"
        st.experimental_rerun()

    side_bar.run(session_state)