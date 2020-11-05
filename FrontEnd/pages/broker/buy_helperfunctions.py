import utilities.requests_server as requests_server
import streamlit as st
# BUY

# LUCA RUF MICH MAL AN

def check_for_entry_string(entry):
    if entry != "N/A":
        return entry
    else:
       return "N/A"


def get_total_stock_value(single_stock_value, quantity):
    if single_stock_value != "N/A":
        return (single_stock_value * quantity)
    else:
        return "N/A"

def get_total_purchase_value(total_stock_value, purchase_fees):
    if total_stock_value != "N/A":
        return (str(total_stock_value + purchase_fees) + "$")
    else:
        return "N/A"

def get_dividend_yield(dividend_yield_raw):
    if dividend_yield_raw != "N/A":
        dividend_yield = round(float((dividend_yield_raw) * 100), 2)
        print(dividend_yield)
        return dividend_yield
    else:
        return "N/A"


def get_image_url(auth_key, logoUrl):
    if logoUrl != "N/A":
        return logoUrl
    else:
        return "https://coolbackgrounds.io/images/backgrounds/white/pure-white-background-85a2a7fd.jpg"

@st.cache(show_spinner=False )
def get_single_stock_value(auth_key, ticker_code):
    stock_price = (requests_server.get_stockprice_history(auth_key, ticker_code, "1d"))[0]
    stock_price = stock_price["stock_price"]
    if stock_price != "N/A":
        return round(float(stock_price), 2)
    else:
        return "N/A"

@st.cache(show_spinner=False )
def get_transaction_fees(auth_key):
    selling_fees = (requests_server.get_user_transaction_fee(auth_key))["transactionFee"]
    return selling_fees

@st.cache(show_spinner=False )
def get_stock_description(auth_key, ticker_code):
    stock_description = requests_server.get_stock_description(auth_key,
                                                              ticker_code)
    return stock_description
# SELL


