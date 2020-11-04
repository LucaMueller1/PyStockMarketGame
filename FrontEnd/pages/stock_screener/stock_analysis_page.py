# PAGE IMPORTS
import pages.side_bar as side_bar

# UTILITIES IMPORTS
import utilities.chart_generator as chart_generator
import utilities.requests_server as requests_server

# MODULES IMPORTS
import streamlit as st

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def run(session_state):

    local_css("FrontEnd/css/style.css")
    description = session_state.stock_desc

    if st.button("🔍 return to search"):
        session_state.stock_desc = None
        st.experimental_rerun()

    st.title(description["stockName"])
    st.markdown(f"""<img src="{description["logoUrl"]}" style="border-radius: 50%">""", unsafe_allow_html=True)

    chart_generator.show_chart()

    general_information = st.beta_expander("general information", expanded=True)
    general_information.write(f"""**Symbol:** {description["symbol"]}""")
    general_information.write(f"""**Country:** {description["country"]}""")
    general_information.write(f"""**Industry:** {description["industry"]}""")
    general_information.write(f"""**Full Time Employees:** {description["fullTimeEmployees"]}""")

    financial_information = st.beta_expander("financial information", expanded=True)
    financial_information.write(f"""**Market Capitalization:** {description["marketCap"]}$""")
    financial_information.write(f"""**Dividend Rate:** {description["dividend"]}""")
    financial_information.write(f"""**52 Week High:** {description["fiftyTwoWeekHigh"]}""")
    financial_information.write(f"""**52 Week Low:** {description["fiftyTwoWeekLow"]}""")

    long_description = st.beta_expander("description")
    long_description.write(f"""'{description["longDescription"]}'""")

    side_bar.run(session_state)
