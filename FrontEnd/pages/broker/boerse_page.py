# PAGE IMPORTS
import pages.side_bar as side_bar
import streamlit as st
from time import sleep

# Utilities IMPORTS
import utilities.requests_server as requests_server
import pages.broker.helperfunctions as hf
from streamlit import caching


def run(session_state):
    side_bar.run(session_state)
    session_state.buy_redirect = False

    # Load CSS File for Formatting
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    local_css("FrontEnd/css/style.css")

    st.title("broker")
    st.subheader("Welcome to your personalised broker. Here you can buy and sell your stocks.")

    mode_switch = st.radio("Please choose whether you want to buy or sell stocks", ("Buy", "Sell"))
    if mode_switch == "Buy":
        if session_state.stock_desc:
            # index = next(session_state.stock_names.index(name) for name in session_state.stock_names if session_state.stock_desc["symbol"] in name) + 1
            index = [i for i, s in enumerate(session_state.stock_names) if session_state.stock_desc["symbol"] in s][
                        0] + 1
        else:
            index = 0

        # Get the ticker_code from the User
        st.write("Please enter your desired stock ticker and the quantity of your purchase:")
        ticker_code_entry_raw = st.selectbox("Stock ticker:", [" "] + session_state.stock_names, index)
        if ticker_code_entry_raw != " ":
            ticker_code_entry = ticker_code_entry_raw.split(": ")[1]

            # Get the quantity from user
            ticker_quantity_entry = st.number_input("Quantity: ", step=1, value=1, min_value=1)
            ticker_quantity_entry = int(ticker_quantity_entry)

            col1, col2 = st.beta_columns(2)

            # Collecting stock information
            single_stock_value = hf.get_single_stock_value(session_state.auth_key, ticker_code_entry) #Y
            total_stock_value = hf.get_total_stock_value(single_stock_value, ticker_quantity_entry) #Y
            purchase_fees = hf.get_transaction_fees(session_state.auth_key) #Y
            total_purchase_value = hf.get_total_purchase_value(total_stock_value, purchase_fees) #Y
            stock_description = hf.get_stock_description(session_state.auth_key, ticker_code_entry) #Y
            stock_name = hf.check_for_entry_string(str(stock_description["stockName"])) #Y
            image_source = hf.get_image_url(session_state.auth_key, stock_description["logoUrl"]) #Y
            dividend_yield = hf.get_dividend_yield(stock_description["dividend"]) #Y
            user_balance = hf.get_user_balance(session_state.auth_key) #Y

            with col1:
                st.write("----------------------")
                st.subheader("Buy - Overview")
                st.write("----------------------")
                st.write("""<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Stock Price: <b><code style="color: black;">""" + str(single_stock_value) + "$" + """</code></b></p></div> """, unsafe_allow_html=True)
                st.write("""<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Stock Quantity: <b><code style="color: black;">""" + str(ticker_quantity_entry) + """</code></b></p></div> """, unsafe_allow_html=True)
                st.markdown("""<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Purchase fees: <code style="color: #F52D5B;">""" + str(purchase_fees) + "$" + """</code></p></div> """, unsafe_allow_html=True)
                st.write("----------------------")
                st.subheader("Total Purchase Price:")
                st.title(total_purchase_value)

                if st.button("Buy"):
                    # send post request to DB
                    buy_response = requests_server.post_transaction(session_state.auth_key,
                                                                    ticker_code_entry,
                                                                    ticker_quantity_entry, transaction_type="buy")
                    user_has_sufficient_cash = hf.check_for_sufficient_cash_user(buy_response)
                    print(user_has_sufficient_cash)
                    if user_has_sufficient_cash is False:
                        st.error("Insufficient funds")
                        sleep(2)
                        st.experimental_rerun()

                    st.write("Your specified stocks have been bought and can be viewed in your portfolio")
                    st.balloons()
                    sleep(2)

                    st.experimental_rerun()

            # Place stock information on the right side
            with col2:
                st.write("---")
                st.write("""
                                <div class="greyish padding">
                                <h2><u>Stock Information<u></h2>
                                <p>Stock name: <b>""" + stock_name + """ </b></p>
                                <p>Stock value: <b>""" + str(single_stock_value) + "$" + """<b></p>
                                <p>Dividend Yield: <b>""" + str(dividend_yield) + "%" + """<b></p>
                                <img class = "circle_and_center" src = """ + image_source + """>
                                </div>
                                """, unsafe_allow_html=True)
                st.write("""<h4>&nbsp</h4>""", unsafe_allow_html=True)
                st.write("""
                                <div class="greyish padding boxes-available-funds">
                                <h4 style="text-align:center;">Available Funds:</h4>
                                <h2 style="text-align:center;">""" + str(user_balance) + "$" + """</h2>
                                </div>
                                """, unsafe_allow_html=True)


    elif mode_switch == "Sell":
        caching.clear_cache()
        session_state.page = "sell"
        st.experimental_rerun()
