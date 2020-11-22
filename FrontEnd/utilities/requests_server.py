"""
    desc:       requests module that is used to communicate with the Back-End
    author:     Luca Weißbeck, Ben Schaper
    date:       2020-11-16
"""
# MODULE IMPORTS
import requests
import streamlit as st

BASE_URL = "http://localhost:8080/api/"


def login(user_name_input: str, password_input: str) -> dict:
    """
    desc:   Authenticates user and returns api key for other requests
    param:  (str) user_name_input, (str) password_input
    test:   pass: user name and password can be found in data base.
            fail:  user name and password can not be found in data base.
    """

    json = {'email': user_name_input,
            'password': password_input}

    return requests.post(BASE_URL + "user/login", json=json).json()

def logout(auth_key: str) -> dict:
    """
    desc:   Deletes auth key in Back-End.
    param:  (str) auth_key
    test:   pass: user is logged in -> log out
            fail:  user is not logged in and performs log out
    """
    return requests.get(BASE_URL + "user/logout", headers={"api_key": auth_key}).json()

def register(first_name: str, name: str, mail: str, password: str, start_capital: float) -> dict:
    """
    desc:   Deletes auth key in Back-End.
    param:  (str) first_name, (str) name, (str) mail, (str) password, (float) start_capital
    test:   pass: all necessary data is provided.
            fail:  first_name or other info is missing.
    """
    json = {'firstName': first_name,
            'lastName': name,
            'email': mail,
            'password': password,
            'startingCapital': start_capital,
            'moneyAvailable': start_capital}

    return requests.post(BASE_URL + "user", json=json).json()

@st.cache(show_spinner=False)
def get_user(auth_key: str) -> dict:
    """
    desc:   This can only be done by the logged in user and will return the user object.
    param:  (str) auth_key
    test:   pass: auth_key is valid
            fail:  auth_key is invalid
    """
    return requests.get(BASE_URL + "user", headers={"api_key": auth_key}).json()

@st.cache(show_spinner=False)
def get_stock_names(auth_key: str) -> dict:
    """
    desc:   This can only be done by the logged in user and will return a user object.
    param:  (str) auth_key
    test:   pass: auth_key is valid
            fail:  auth_key is invalid
    """
    return requests.get(BASE_URL + "stock", headers={"api_key": auth_key}).json()

def get_combined_stock_names(auth_key: str) -> list:
    """
    desc:   Automatically combines and returns all stock symbols and names in a list.
    param:  (str) auth_key
    test:   pass: auth_key is valid
            fail:  auth_key is invalid
    """
    return [f"""{stock_dict["stockName"]}: {stock_dict["symbol"]}""" for stock_dict in get_stock_names(auth_key)]

def post_transaction(auth_key: str, symbol: str, amount: float, transaction_type: str):
    """
    Send transaction details to backend, once a user buys or sells a stock in frontend.

    :param auth_key: (String) API key authorizing and identifying the user.
    :param symbol: (String) Stock selected by user
    :param amount: (Float) Total selling value or buy value.
    :param transaction_type: (String) "buy" or "sell"
    :return: (Dictionary)
    :test Correct: All parameters are specified with the correct datatype and API request is successful. Incorrect: Typo in transaction_type --> API request fails.
    """
    json = {"symbol": symbol,
            "amount": amount,
            "transactionType": transaction_type}
    return requests.post(BASE_URL + "portfolio/transaction", headers={"api_key": auth_key}, json=json)

def get_stock_description(auth_key: str, symbol: str) -> dict:
    """
    desc:   Returns financials which include dividend, p/e-value and much more
    param:  (str) auth_key, (str) symbol
    test:   pass: auth_key is valid and symbol exists
            fail:  auth_key is invalid or symbol does not exist
    """
    return requests.get(BASE_URL + f"stock/{symbol}/description", headers={"api_key": auth_key}).json()

@st.cache(show_spinner=False)
def get_stockprice_history(auth_key: str, symbol: str, period: str):
    """
    Returns stockprice history for specified period. This includes the stock price with a timestamp.

    :param auth_key: (String) API key authorizing and identifying the user.
    :param symbol: (String) Stock selected by user
    :param period: (String) Example: 1d stands for one day.
    :return: (List) Returns a List with dictionaries inside.
    :test Correct: Method is called using a valid authkey, valid symbol and a valid period and the API request is successful. Incorrect: Period input-parameter is invalid or specified incorrectly and API request fails.
    """
    return requests.get(BASE_URL + f"stock/{symbol}/history?period={period}", headers={"api_key": auth_key}).json()

def get_user_transaction_fee(auth_key: str):
    """
    API request to obtain current transaction fee from backend.

    :param auth_key: (String) API key authorizing and identifying the user.
    :return: (Dictionary)
    :test Correct: Valid auth_key is provided and API request is successful. Incorrect: No auth_key is provided and API request fails.
    """
    return requests.get(BASE_URL + "user/settings", headers={"api_key": auth_key}).json()

@st.cache(show_spinner=False)
def get_user_portfolio(auth_key: str) -> dict:
    """
    desc:   Returns all the current stock positions of the logged in user
    param:  (str) auth_key
    test:   pass: auth_key is valid
            fail:  auth_key is invalid
    """
    return requests.get(BASE_URL + "portfolio", headers={"api_key": auth_key}).json()

def delete_user(auth_key: str):
    """
    API request to delete user.

    :param auth_key: (String) API key authorizing and identifying the user.
    :return: (Dictionary)
    :test Correct: Valid auth key is provided and API request is successful. Incorrect: No auth key is supplied and API request fails.
    """
    return requests.delete(BASE_URL + "user", headers={"api_key": auth_key}).json()

def post_settings(auth_key:str, transactionFee: float):
    """
    API request to update the transaction fees in Backend, when user adjusts TransactionFees in Frontend.

    :param auth_key: (String) API key authorizing and identifying the user.
    :param transactionFee: (Float) Float for new transaction fee
    :return: (Dictionary)
    :test Correct: Valid auth key and a float for transactionFee is provided, API request successful. Incorrect: transactionFee is passed as a String into the method and API request fails.
    """
    json = {"transactionFee": transactionFee}
    return requests.post(BASE_URL + "user/settings", headers={"api_key": auth_key}, json=json)

def get_sustainability_info(auth_key: str, symbol: str) -> list:
    """
    desc:   Returns sustainability info for one symbol
    param:  (str) auth_key, (str) symbol
    test:   pass: auth_key is valid and symbol exists
            fail:  auth_key is invalid or symbol does not exist
    """
    return requests.get(BASE_URL + f"stock/{symbol}/sustainability", headers={"api_key":auth_key}).json()

@st.cache(show_spinner=False)
def get_portfolio_history(auth_key: str) -> dict:
    """
    desc:   Returns the logged in users portfolio performance (historical portfolio data)
    param:  (str) auth_key
    test:   pass: auth_key is valid
            fail:  auth_key is invalid
    """
    return requests.get(BASE_URL + "portfolio/value", headers={"api_key": auth_key}).json()