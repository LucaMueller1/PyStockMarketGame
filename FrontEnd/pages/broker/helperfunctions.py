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
    :return: (String) If the input parameter total_stock_value does not equal "N/A" the function outputs a String representing the total_stock_value including the purchase fees. Otherwise it will return "N/A"
    :test Correct: Method is called using a valid (Float) total_stock_value and a valid (Float) purchase_fee, thus returning a string for the total_purchase_value. Incorrect: Either parameter is of type string --> The method will return the string "N/A"
    """

    if total_stock_value != "N/A":
        total_purchase_value = round((float(total_stock_value) + float(purchase_fees)), 2)
        return (str(total_purchase_value) + "$")
    else:
        return "N/A"


def get_dividend_yield(dividend_yield_raw):
    """
    Calculates the dividend yield in percentage and rounds the result to two decimals.

    :param dividend_yield_raw: (Float) Dividend yield is part of the stock description acquired in the buy page.
    :return: (Float) calculated dividend yield.
    :test Correct: Method is called using a valid float and thus returns a further processed float. Incorrect: Method is called using a String, it will then return the string "N/A"
    """

    if dividend_yield_raw != "N/A":
        dividend_yield = round(float((dividend_yield_raw) * 100), 2)
        return dividend_yield
    else:
        return "N/A"


def get_image_url(logoUrl):
    """
    Ensures that the image URL is valid. If the image URL is invalid, the function returns a white image.

    :param logoUrl: (String) logoUrl is part of the stock description acquired in the buy page.
    :return: (String) returns the method parameter as long as it does not equal "N/A"
    :test Correct: Method is called using a valid URL string. The method subsequently returns the input URL. Incorrect: Method is called using an integer which will return a blank white image.
    """
    if logoUrl != "N/A":
        return logoUrl
    else:
        return "https://coolbackgrounds.io/images/backgrounds/white/pure-white-background-85a2a7fd.jpg"


def check_for_sufficient_cash_user(buy_response):
    """
    Ensures that the user has sufficient cash in his portfolio by analysing the response which is returned by the API after committing the buy transaction.

    :param buy_response: (Response object) response received from API after committing the buy on the buy page.
    :return: (Boolean) returns True or False depending on the reponse object of the API request.
    :test Correct: Method is called using a valid response object (e.g.: {'amount': 1, 'id': 24, 'stockValue': {'id': 25, 'stock_price': 161.59, 'symbol': 'AAP', 'timestamp': '2020-11-09T00:00:00Z'}, 'transactionFee': 10, 'transactionType': 'buy'}
    ). A "True" boolean is subsequently returned. Incorrect: Method is called using a reponse type object which status equals 400 and therefore returns False.
    """
    buy_response = json.loads(buy_response.text)
    print(buy_response)
    if ("status" in buy_response):
        if (buy_response["status"] == 400):
            sufficient_cash = False
            return sufficient_cash
    else:
        sufficient_cash = True
        return sufficient_cash


@st.cache(show_spinner=False)
def get_depo_array(auth_key):
    """
    API GET request for different stocks in user portfolio is written into a list.

    :param auth_key: (String) API key authorizing and identifying the user.
    :return: depo_array --> (List), user_portfolio --> (List)
    :test Correct: A valid auth_key is provided in order for the GET request to the API to work. Both the depo array and the user portfolio is acquired and returned. Incorrect: No auth key is provided leading to a failed GET request and returning a 401 unauthorized error.
    """
    user_portfolio = requests_server.get_user_portfolio(auth_key)
    depo_array = []
    for item in user_portfolio:
        depo_array.append(item["symbol"] + ": " + item["stockName"])
    return depo_array, user_portfolio


def get_stock_quantity_in_depot(depot_information, stock_ticker):
    """
    Retrieve the stock quantity in portfolio for a selected stock from the user.

    :param depot_information: (List) This is the second return parameter returned from the get_depo_array function.
    :param stock_ticker: (String) Stock selected by user
    :return: (Int) Quantity of selected stock in portfolio
    :test Correct: A valid list for depot information is being passed into the method as well as a valid stock ticker. The stock ticker can be found in the portfolio information and the quantity of the specific stock in the portfolio can be returned. Incorrect: A valid list for stock description is passed into the method, however the stock ticker can not be found inside the description.
    """
    for item in depot_information:
        if item["symbol"] == stock_ticker:
            return item["amount"]



def get_buyin_for_stock(depot_information, stock_ticker):
    """
    Retrieve the  buy in price for a selected stock from user.

    :param depot_information: (List) This is the second return parameter returned from the get_depo_array function.
    :param stock_ticker: (String) Stock selected by user
    :return: (Float) Buy in price of selected stock in portfolio
    :test Correct: A valid list for depot information is passed into the method as well as a valid stock ticker. Therefore, the buy in price for the specified stock ticker will be returned. Incorrect: Instead of a list for depot information a numerical value such as an integer is passed into the method leading to an error in the for loop.
    """
    for item in depot_information:
        if item["symbol"] == stock_ticker:
            return float(item["stock_buyin_price"])


def gethtml_for_change_buyin_current(stock_buyin, single_stock_price):
    """
    Returns HTML element containing the total change of the stock from the buyin price to the current price.

    :param stock_buyin: (Float) Buy in price for specfic stock retrieved from depot_information using the get_buyin_for_stock method.
    :param single_stock_price: (Float) Most recent value in stock market for stock specified. Calculated using the get_single_stock_value method.
    :return: (HTML string) The return is a String containing HTML elements, thus the method can easily be implemented into an st.write method using HTML by concatenating the return of this function with the rest of the st.write function.
    :test Correct: Method is called with a valid stock_buyin float as well as a valid single_stock_price float. Depending on the calculated change in the method, this will return a different string, which can be concatenated into an HTML element. Incorrect: Method is called without any parameter input resulting in an error at the change calculation, as no elements are provided to calculate the change with.
    """
    change = round((float(single_stock_price) - float(stock_buyin)), 2)
    if change < 0:
        change = str(change) + "$"
        return """<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Change per stock since buy: <code style="color: #F52D5B;">""" + change + """</code></p></div> """
    else:
        change = "+" + str(change) + "$"
        return """<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Change per stock since buy: <code>""" + change + """</code></p></div> """


def calculate_total_change(stock_buyin, single_stock_price, stock_quantity):
    """
    Calculates the total change for a specific stock from buyin value to current current.

    :param stock_buyin: (Float) Buy in price for specfic stock retrieved from depot_information using the get_buyin_for_stock method.
    :param single_stock_price: (Float) Most recent value in stock market for stock specified. Calculated using the get_single_stock_value method.
    :param stock_quantity: (Int) The quantity of chosen stock by user in portfolio.
    :return: (HTML string) Both returns consists of an HTML String. They differentiate by the colour printed in Frontend. --> If change is negative (red colour) --> If change is positive (green colour)
    :test Correct: Parameter stock_buyin, single_stock_price are passed as a Float, stock_quantity is passed as an Integer, therefore the total change can be calculated successfully and the corresponding HTML string is returned. Incorrect: A parameter is missed as an input, such as the stock quantity. The method will fail at calculating the total change.
    """
    total_change = round((float(single_stock_price * stock_quantity) - float(stock_buyin * stock_quantity)), 2)
    if total_change < 0:
        total_change = str(total_change) + "$"
        return """<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Total Change: <code style="color: #F52D5B;">""" + total_change + """</code></p></div> """
    else:
        total_change = "+" + str(total_change) + "$"
        return """<div class="markdown-text-container stMarkdown" style="width: 349px;"><p>Total Change: <code>""" + total_change + """</code></p></div> """

def get_user_balance(auth_key):
    """
    Returns the users portfolio balance by authorizing a get request and acquiring the attribute "moneyAvailable" in the User object.

    :param auth_key: (String) API key authorizing and identifying the user.
    :return: (String) User balance is returned as a string.
    :test Correct: the request is successful with a valid auth_key and returns a user object with the attribute "moneyAvailable" Incorrect: The method is called using an invalid auth key resulting in a failed get request.
    """
    user = requests_server.get_user(auth_key)
    user_balance = user["moneyAvailable"]
    return user_balance

def get_sustainability_info(auth_key, stock_ticker):
    """
    Returns a list of warnings for a specific stock chosen by the user by processing an API request and looping through the returned dictionary for keys holding the boolean value True. The corresponding value of said key is written into an array.

    :param auth_key: (String) API key authorizing and identifying the user.
    :param stock_ticker: (String) Stock selected by user
    :return: (List) List of warnings for a specific stock
    :test Correct: A valid auth_key is supplied, as well as a valid stock ticker. Thus the Get request will succeed and the loop through the returned dictionary is functional and the created list of warnings is returned. Incorrect: The Get request fails due to an invalid auth key. Thus the loop is rendered non functional and returns an error.
    """
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

