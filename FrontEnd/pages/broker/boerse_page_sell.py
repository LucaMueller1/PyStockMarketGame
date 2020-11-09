# Pages Import
import pages.side_bar as side_bar

# Modules Import
import streamlit as st
from streamlit import caching
from time import sleep

# Utilities Import
import utilities.requests_server as requests_server
import pages.broker.helperfunctions as hf
import utilities.utils as utils


def run(session_state):
    side_bar.run(session_state)
    utils.local_css("FrontEnd/css/style.css")

    st.title("Broker")
    st.subheader("Welcome to your personalised broker. Here you can buy and sell your stocks.")

    # switch between BUY and SELL
    mode_switch = st.radio("Please choose whether you want to buy or sell stocks", ("Buy", "Sell"))
    if mode_switch == "Sell":
        st.write("Please choose the stock, that you want to sell.")

        depot_array, depot_information = hf.get_depo_array(session_state.auth_key)
        ticker_code_entry_raw = st.selectbox("Stock ticker:", [" "] + depot_array)
        if ticker_code_entry_raw != " ":
            ticker_code_entry = ticker_code_entry_raw.split(": ")[0]
            quantity_in_user_portfolio = int(hf.get_stock_quantity_in_depot(depot_information, ticker_code_entry))

            if st.checkbox("Sell all stocks", value=True):
                # Set the Value of quantity to the amount user has in Depot
                stock_quantity_for_sale = quantity_in_user_portfolio

            else:
                col1, col2 = st.beta_columns((4, 1))

                # Selection of quantity
                with col1:
                    quantity_input_method_choice = st.radio("Input method", ("Slider", "TextInput"))

                    # Slider
                    if quantity_input_method_choice == "Slider":
                        stock_quantity_for_sale = st.slider("Please choose the quantity of stocks", 1,
                                                            quantity_in_user_portfolio)

                    # Textfeld & Button
                    if quantity_input_method_choice == "Textfield":
                        stock_quantity_for_sale_raw = st.number_input("Please choose the quantity of stocks",
                                                                      min_value=1,
                                                                      max_value=quantity_in_user_portfolio,
                                                                      step=1, value=1)
                        stock_quantity_for_sale = int(stock_quantity_for_sale_raw)

                # Anzeige der Quantität der ausgewaählten Aktie im Depot
                with col2:
                    st.markdown("""
                            <div class="greyish padding">
                            <h4>Quantity in Depot</h4>
                            <h1 style="text-align:center;">""" + str(quantity_in_user_portfolio) + """</h1>
                            </div>
                            """, unsafe_allow_html=True)

            # Get stockinformation
            single_stock_price = hf.get_single_stock_value(session_state.auth_key, ticker_code_entry)
            selling_fees = hf.get_transaction_fees(session_state.auth_key)
            stock_sell_value_price = round(float(stock_quantity_for_sale * single_stock_price), 2)
            total_sell_value = str(round((stock_sell_value_price - float(selling_fees)), 2)) + "$"
            stock_description = hf.get_stock_description(session_state.auth_key, ticker_code_entry)
            stock_name = str(stock_description["stockName"])
            dividend_yield = hf.get_dividend_yield(stock_description["dividend"])
            image_source = hf.get_image_url(session_state.auth_key, (stock_description["logoUrl"]))
            stock_buyin_price = hf.get_buyin_for_stock(depot_information, ticker_code_entry)

            # Auflistung Verkaufspreis mit Ordergebühren
            col1, col2 = st.beta_columns(2)
            with col1:
                st.write("---")
                st.subheader("Sell - Overview")
                st.write("---")
                st.write("""<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Stock Quantity: <b><code style="color: black;">""" + str(stock_quantity_for_sale) + """</code></b></p></div> """, unsafe_allow_html=True)
                st.write("""<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Transaction Value: <b><code style="color: black;">""" + str(stock_sell_value_price) + "$" + """</code></b></p></div> """, unsafe_allow_html=True)
                st.write("""<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Selling Fees: <code style="color: #F52D5B;">""" + str(selling_fees) + "$" + """</code></p></div> """, unsafe_allow_html=True)
                st.write("---")
                st.write(hf.rename_calculate_change_buyin_current(stock_buyin_price, single_stock_price), unsafe_allow_html=True)
                st.write(hf.calculate_total_change(stock_buyin_price, single_stock_price, stock_quantity_for_sale), unsafe_allow_html=True)
                st.write("---")
                st.subheader("Total selling value:")
                st.title(total_sell_value)
                print(stock_buyin_price)

                # Sell button
                if st.button("Sell"):
                    sell_response = requests_server.post_transaction(session_state.auth_key,
                                                                     ticker_code_entry,
                                                                     stock_quantity_for_sale, transaction_type="sell")
                    st.subheader("Sold")
                    caching.clear_cache()
                    session_state.page = "boerse"
                    st.experimental_rerun()

            # Aktieninformationen neben der Verkaufsauflistung anzeigen
            with col2:
                st.write("---")
                st.markdown("""
                                            <div class="greyish padding">
                                            <h2><u>Stock Information</u></h2>
                                            <p>Stock name: <b>""" + str(stock_name) + """ </b></p>
                                            <p>Single stock value: <b>""" + str(single_stock_price) + "$" + """<b></p>
                                            <p>Dividend Yield: <b>""" + str(dividend_yield) + "%" + """<b></p>
                                            <img class = "circle_and_center" src = """ + image_source + """>
                                            </div>
                                            """, unsafe_allow_html=True)

    elif mode_switch == "Buy":
        session_state.page = "boerse"
        st.experimental_rerun()
