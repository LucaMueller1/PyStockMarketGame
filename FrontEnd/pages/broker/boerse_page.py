# PAGE IMPORTS
import pages.side_bar as side_bar
import streamlit as st
from time import sleep

# Utilities IMPORTS
import utilities.requests_server as requests_server


def run(session_state):

    side_bar.run(session_state)
    # Load CSS File for Formatting
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    local_css("FrontEnd/css/style.css")

    st.title("broker")
    st.subheader("Welcome to your personalised broker. Here you can buy and sell your stocks.")

    # switch between BUY and SELL
    mode_switch = st.radio("Please choose whether you want to buy or sell stocks", ("Buy", "Sell"))

    if mode_switch == "Buy":
        mode = "buy"
        test_array = []
        if session_state.stock_id:
            test_array.append(session_state.stock_id)
        else:
            test_array.append(" ")
        # Get the ticker_code from the User
        st.write("Please enter your desired stock ticker and the quantity of your purchase:")
        ticker_code_entry = st.selectbox("Stock ticker:", test_array + session_state.stock_names)

        if ticker_code_entry != " ":
            # Splitting the ticker_code from the stock name
            ticker_code_entry_for_post_request = ticker_code_entry.split(": ")[1]

            # Get the quantity from user
            ticker_quantity_entry = st.number_input("Quantity: ", step = 1.0)
            ticker_quantity_entry = int(ticker_quantity_entry)

            # If button is clicked --> Entry submitted (quantity & ticker_code)
            if st.button("Apply"):
                session_state.buy_redirect = True

            if session_state.buy_redirect:
                # We are only defining the layout here in order to split the page into two parts.
                # The lefthand part will be filled with the total amount and the "Kaufen" button
                # Righthand part will be filled with Aktieninfos (Aktienname, Aktienwert, Dividendenrendite, Symbol)
                col1, col2 = st.beta_columns(2)

                # specific_stock_value is calculated by 190 (later changed to chosen Stock from ticker_code_entry) times the amount chosen by user
                specific_stock_value = 190 * int(ticker_quantity_entry)

                # purchase_fees is static for now, but will later be fetched from database
                purchase_fees = 9.90

                # dividen_yield is static for now, but will later be fetched from database
                dividend_yield_raw = 0.06
                dividend_yield = str(dividend_yield_raw * 100) + "%"

                # Add purchase_fees to specific_stock_value
                total_purchase_value = str(specific_stock_value + purchase_fees) + "€"

                # Place price information and "Kaufen" button on the left side
                with col1:
                    st.subheader("Buy - Overview")
                    st.write("----------------------")
                    st.write("Stock price:", specific_stock_value)
                    st.write("Purchase fees:", purchase_fees)
                    st.write("----------------------")
                    st.subheader("Total purchase price:")
                    st.title(total_purchase_value)

                    if st.button("Buy"):
                        # send post request to DB
                        response = requests_server.post_transaction(session_state.auth_key, ticker_code_entry_for_post_request,
                                                                        ticker_quantity_entry, transactionType="buy")

                        st.write("You can view your purchased stocks in your depot.")
                        sleep(2)

                        session_state.buy_redirect = False
                        st.experimental_rerun()

                        # This is where the actual buy happens
                        # Once connected to BE: Get Price of chosen stock & fee --> Calculate end price

                # Place stock information on the right side
                with col2:
                    st.markdown("""
                                    <div class="greyish padding">
                                    <h2>Stock information</h2>
                                    <p>Stock name: <b>Adidas</b></p>
                                    <p>Stock value: <b>""" + "190" + """<b></p>
                                    <p>Dividendyield: <b>""" + dividend_yield + """<b></p>
                                    <img class = "circle_and_center" src = "https://logo.clearbit.com/apple.com">
                                    </div>
                                    """
                                , unsafe_allow_html=True)


    elif mode_switch == "Sell":
        session_state.page = "sell"
        st.experimental_rerun()

