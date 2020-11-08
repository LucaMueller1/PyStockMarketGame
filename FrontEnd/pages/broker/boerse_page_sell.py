# Pages Import
import pages.side_bar as side_bar

# Modules Import
import streamlit as st
from streamlit import caching
# Utilities Import
import utilities.requests_server as requests_server
import pages.broker.helperfunctions as hf
from time import sleep


def run(session_state):
    side_bar.run(session_state)

    # Load CSS File for Formatting
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    local_css("FrontEnd/css/style.css")

    st.header("Broker")
    st.subheader("Welcome to your personalised broker. Here you can buy and sell your stocks.")

    # switch between BUY and SELL
    mode_switch = st.radio("Please choose whether you want to buy or sell stocks", ("Buy", "Sell"))
    if mode_switch == "Sell":
        st.write("Please choose the stock, that you want to sell.")

        depot_array, depot_information = hf.get_depo_array(session_state.auth_key)
        ticker_code_entry = st.selectbox("Stock ticker:", [" "] + depot_array)
        if ticker_code_entry != " ":
            ticker_code_entry_for_post_request = ticker_code_entry.split(": ")[0]
            maximum_available_quantity_for_stock = int(
                hf.get_stock_quantity_in_depot(depot_information, ticker_code_entry_for_post_request))

            if st.checkbox("Sell all stocks", value=True):
                # Set the Value of quantity to the amount user has in Depot
                stock_quantity_for_sale = maximum_available_quantity_for_stock

            else:
                col1, col2 = st.beta_columns((4, 1))

                # Selection of quantity
                with col1:
                    quantity_input_method_choice = st.radio("Input method", ("Slider", "Textfield"))

                    # Slider
                    if quantity_input_method_choice == "Slider":
                        stock_quantity_for_sale = st.slider("Please choose the quantity of stocks", 1,
                                                            maximum_available_quantity_for_stock)

                    # Textfeld & Button
                    if quantity_input_method_choice == "Textfield":
                        stock_quantity_for_sale_raw = st.number_input("Please choose the quantity of stocks",
                                                                      min_value=1,
                                                                      max_value=maximum_available_quantity_for_stock,
                                                                      step=1, value=1)
                        stock_quantity_for_sale = int(stock_quantity_for_sale_raw)

                # Anzeige der Quantität der ausgewaählten Aktie im Depot
                with col2:
                    st.markdown("""
                            <div class="greyish padding">
                            <h4>Quantity in Depot</h4>
                            <h1 style="text-align:center;">""" + str(maximum_available_quantity_for_stock) + """</h1>
                            </div>
                            """, unsafe_allow_html=True)

            # Get stockinformation
            single_stock_price = hf.get_single_stock_value(session_state.auth_key, ticker_code_entry_for_post_request)
            selling_fees = hf.get_transaction_fees(session_state.auth_key)
            stock_sell_value_price = round(float(stock_quantity_for_sale * single_stock_price), 2)
            total_sell_value = str(round((stock_sell_value_price - float(selling_fees)), 2)) + "$"

            stock_description = hf.get_stock_description(session_state.auth_key, ticker_code_entry_for_post_request)
            stock_name = str(stock_description["stockName"])
            dividend_yield = hf.get_dividend_yield(stock_description["dividend"])
            image_source = hf.get_image_url(session_state.auth_key, (stock_description["logoUrl"]))

            # Auflistung Verkaufspreis mit Ordergebühren
            col1, col2 = st.beta_columns(2)
            with col1:
                st.write("----------------------")
                st.subheader("Sell - Overview")
                st.write("----------------------")
                st.write("Selected Quantity:", stock_quantity_for_sale)
                st.write("Transaction value ($):", stock_sell_value_price)
                st.markdown(
                    """<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Purchase fees ($): <code style="color: #F52D5B;">""" + str(
                        hf.check_for_entry_string(selling_fees)) + """</code></p></div> """, unsafe_allow_html=True)
                st.write("----------------------")
                st.subheader("Total selling value:")
                st.title(total_sell_value)
                st.subheader("+/-:")

                # Sell button
                if st.button("Sell"):
                    st.subheader("Sold")
                    sell_response = requests_server.post_transaction(session_state.auth_key,
                                                                     ticker_code_entry_for_post_request,
                                                                     stock_quantity_for_sale, transaction_type="sell")

            # Aktieninformationen neben der Verkaufsauflistung anzeigen
            with col2:
                st.markdown("""
                                            <div class="greyish padding">
                                            <h2><u>Stock Information</u></h2>
                                            <p>Stock name: <b>""" + stock_name + """ </b></p>
                                            <p>Single stock value: <b>""" + str(single_stock_price) + "$" + """<b></p>
                                            <p>Dividend yield (%): <b>""" + str(dividend_yield) + """<b></p>
                                            <img class = "circle_and_center" src = """ + image_source + """>
                                            </div>
                                            """, unsafe_allow_html=True)

    elif mode_switch == "Buy":
        caching.clear_cache()
        session_state.page = "boerse"
        st.experimental_rerun()
