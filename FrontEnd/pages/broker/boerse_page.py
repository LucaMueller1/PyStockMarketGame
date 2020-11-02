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
    st.subheader("Willkommen zur Börse. Hier kannst du Wertpapiere kaufen oder deine vorhandenen Wertpapiere verkaufen.")

    # switch between BUY and SELL
    mode_switch = st.radio("Bitte wähle aus, ob du Werpapiere kaufen oder verkaufen möchtest", ("Kaufen", "Verkaufen"))

    if mode_switch == "Kaufen":
        mode = "buy"
        test_array = []
        if session_state.stock_id:
            test_array.append(session_state.stock_id)
        else:
            test_array.append(" ")
        # Get the WKN from the User
        st.write("Gib hier eine Wertpapier Kennnummer (WKN) ein, sowie die Anzahl der zu kaufenden Aktien")
        ticker_code_entry = st.selectbox("WKN:", test_array + session_state.stock_names)

        if ticker_code_entry != " ":
            # Splittin the stock ticker from the stock name
            ticker_code_entry_for_post_request = ticker_code_entry.split(": ")[1]

            # Get the quantity from user
            ticker_quantity_entry = st.number_input("Anzahl:", step = 1.0)
            ticker_quantity_entry = int(ticker_quantity_entry)

            # If button is clicked --> Entry submitted (quantity & stock ticker)
            if st.button("Eingabe bestaetigen"):
                session_state.buy_redirect = True

            if session_state.buy_redirect:
                # We are only defining the layout here in order to split the page into two parts.
                # The lefthand part will be filled with the total amount and the "Kaufen" button
                # Righthand part will be filled with Aktieninfos (Aktienname, Aktienwert, Dividendenrendite, Symbol)
                col1, col2 = st.beta_columns(2)

                # Aktienwert is calculated by 190 (later changed to chosen Stock from ticker_code_entry) times the amount chosen by user
                specific_stock_value = 190 * int(ticker_quantity_entry)

                # Gebuehren is static for now, but will later be fetched from database
                purchase_fees = 9.90

                # Dividendenrendite is static for now, but will later be fetched from database
                dividend_yield_raw = 0.06
                dividend_yield = str(dividend_yield_raw * 100) + "%"

                # Add Gebuehren to specific_stock_value
                purchase_value = str(specific_stock_value + purchase_fees) + "€"

                # Place price information and "Kaufen" button on the left side
                with col1:
                    st.subheader("Verkaufsübersicht")
                    st.write("----------------------")
                    st.write("Aktienkaufpreis:", specific_stock_value)
                    st.write("Gebühren:", "", purchase_fees)
                    st.write("----------------------")
                    st.subheader("Kaufpreis:")
                    st.title(purchase_value)

                    if st.button("Buy"):
                        # send post request to DB
                        response = requests_server.post_transaction(session_state.auth_key, ticker_code_entry_for_post_request,
                                                                        ticker_quantity_entry, transactionType="buy")

                        st.write("Du kannst deine gekauften Aktien nun im Depot beobachten.")
                        sleep(2)

                        session_state.buy_redirect = False
                        st.experimental_rerun()

                        # This is where the actual buy happens
                        # Once connected to BE: Get Price of chosen stock & fee --> Calculate end price

                # Place Stock information on the right side
                with col2:
                    st.markdown("""
                                    <div class="greyish padding">
                                    <h2>Aktieninformationen</h2>
                                    <p>Aktienname: <b>Adidas</b></p>
                                    <p>Aktienwert: <b>""" + "190" + """<b></p>
                                    <p>Dividendenrendite: <b>""" + dividend_yield + """<b></p>
                                    <img class = "circle_and_center" src = "https://logo.clearbit.com/apple.com">
                                    </div>
                                    """
                                , unsafe_allow_html=True)


    elif mode_switch == "Verkaufen":
        session_state.page = "sell"
        st.experimental_rerun()

