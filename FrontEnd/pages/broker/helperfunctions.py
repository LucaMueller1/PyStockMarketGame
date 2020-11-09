import utilities.requests_server as requests_server
import streamlit as st
import json


def get_total_stock_value(single_stock_value, quantity):
    """
    Calculates the total stock value by multiplying the current stock value, chosen by the user, value by the wanted quantity.

    :param single_stock_value: (Float) Current value for stock chosen by user
    :param quantity: (Int) Selected quantity by user
    :return: (Float) If the input parameter "single_stock_value" does not equal "N/A" the function outputs a float representing the total stock value. Otherwise it will return "N/A"
    :test Correct: Method is called using a valid (Float) single_stock_value and a valid (Int) quantity, thus returning a float for the total stock value. Incorrect: Either parameter is of type string --> The method will return the string "N/A"
    """
    if single_stock_value != "N/A":
        return single_stock_value * quantity
    else:
        return "N/A"


def get_total_purchase_value(total_stock_value, purchase_fees):
    """
    Calculates the total purchase value by adding the purchase_fees onto the total_stock_value and rounding the calcuting to two decimals.

    :param total_stock_value: (Float) The total_stock_value is made up by the current_stock_value for the stock chosen by the user multiplied by the quantity chosen by the user.
    :param purchase_fees: (Float) The purchase fees can manually be set by the user and represent a fixed value, which is added upon every purchase. This can range from 1$ to 30$ in 0.5$ steps.
    :return: If the input parameter total_stock_value does not equal "N/A" the function outputs a String representing the total_stock_value including the purchase fees. Otherwise it will return "N/A"
    :test Correct: Method is called using a valid (Float) total_stock_value and a valid (Float) purchase_fee, thus returning a string for the total_purchase_value. Incorrect: Either parameter is of type string --> The method will return the string "N/A"
    """

    if total_stock_value != "N/A":
        total_purchase_value = round((float(total_stock_value) + float(purchase_fees)), 2)
        return (str(total_purchase_value) + "$")
    else:
        return "N/A"


def get_dividend_yield(dividend_yield_raw):
    if dividend_yield_raw != "N/A":
        dividend_yield = round(float((dividend_yield_raw) * 100), 2)
        return dividend_yield
    else:
        return "N/A"


def get_image_url(auth_key, logoUrl):
    if logoUrl != "N/A":
        return logoUrl
    else:
        return "https://coolbackgrounds.io/images/backgrounds/white/pure-white-background-85a2a7fd.jpg"


def check_for_sufficient_cash_user(sellresponse):
    sellresponse = json.loads(sellresponse.text)
    if ("status" in sellresponse):
        if (sellresponse["status"] == 400):
            sufficient_cash = False
            return sufficient_cash
    else:
        sufficient_cash = True
        return sufficient_cash


@st.cache(show_spinner=False)
def get_depo_array(auth_key):
    user_portfolio = requests_server.get_user_portfolio(auth_key)
    depo_array = []
    for item in user_portfolio:
        depo_array.append(item["symbol"] + ": " + item["stockName"])
    return depo_array, user_portfolio


def get_stock_quantity_in_depot(depot_information, stock_ticker):
    for item in depot_information:
        if item["symbol"] == stock_ticker:
            return item["amount"]


def get_buyin_for_stock(depot_information, stock_ticker):
    for item in depot_information:
        if item["symbol"] == stock_ticker:
            return float(item["stock_buyin_price"])


def rename_calculate_change_buyin_current(stock_buyin, single_stock_price):
    change = round((float(single_stock_price) - float(stock_buyin)), 2)
    if change < 0:
        change = str(change) + "$"
        return """<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Change per stock since buy: <code style="color: #F52D5B;">""" + change + """</code></p></div> """
    else:
        change = "+" + str(change) + "$"
        return """<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Change per stock since buy: <code>""" + change + """</code></p></div> """


def calculate_total_change(stock_buyin, single_stock_price, stock_quantity):
    total_change = round((float(single_stock_price * stock_quantity) - float(stock_buyin * stock_quantity)), 2)
    if total_change < 0:
        total_change = str(total_change) + "$"
        return """<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Total Change: <code style="color: #F52D5B;">""" + total_change + """</code></p></div> """
    else:
        total_change = "+" + str(total_change) + "$"
        return """<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Total Change: <code>""" + total_change + """</code></p></div> """

def get_user_balance(auth_key):
    user = requests_server.get_user(auth_key)
    user_balance = user["moneyAvailable"]
    return user_balance

def get_sustainability_info(auth_key, stock_ticker):
    sustainability_info = requests_server.get_sustainability_info(auth_key, stock_ticker)
    sustainability_warning_list = []
    for key in sustainability_info:
        if sustainability_info[key] == True:
            sustainability_warning_list.append(key)
    return sustainability_warning_list

def build_warning_html(sustainability_warning_list):
    return_string = ""
    if len(sustainability_warning_list) > 0:
        for item in sustainability_warning_list:
            return_string = return_string + "⚠️ " + item.title() + """<p>&nbsp</p>"""
        return return_string
    else:
        return_string = "✅No apparent warnings found."
        return return_string
@st.cache(show_spinner=False)
def get_single_stock_value(auth_key, ticker_code):
    stock_price = (requests_server.get_stockprice_history(auth_key, ticker_code, "1d"))[0]
    stock_price = stock_price["stock_price"]
    if stock_price != "N/A":
        return round(float(stock_price), 2)
    else:
        return "N/A"


@st.cache(show_spinner=False)
def get_transaction_fees(auth_key):
    transaction_fees = (requests_server.get_user_transaction_fee(auth_key))["transactionFee"]
    return transaction_fees


@st.cache(show_spinner=False)
def get_stock_description(auth_key, ticker_code):
    stock_description = requests_server.get_stock_description(auth_key,
                                                              ticker_code)
    return stock_description

