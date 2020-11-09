import requests
import streamlit as st

BASE_URL = "http://localhost:8080/api/"


def login(user_name_input: str, password_input: str) -> requests.Response:
    json = {'email': user_name_input,
            'password': password_input}

    return requests.post(BASE_URL + "user/login", json=json).json()

def logout(auth_key: str):
    return requests.get(BASE_URL + "user/logout", headers={"api_key": auth_key}).json()

def register(first_name: str, name: str, mail: str, password: str, start_capital: float):
    json = {'firstName': first_name,
            'lastName': name,
            'email': mail,
            'password': password,
            'startingCapital': start_capital,
            'moneyAvailable': start_capital}

    return requests.post(BASE_URL + "user", json=json)

@st.cache(show_spinner=False)
def get_user(auth_key: str) -> str:
    return requests.get(BASE_URL + "user", headers={"api_key": auth_key}).json()

@st.cache(show_spinner=False)
def get_stock_names(auth_key: str) -> requests.Response:
    return requests.get(BASE_URL + "stock", headers={"api_key": auth_key}).json()

def get_combined_stock_names(auth_key):
    return [f"""{stock_dict["stockName"]}: {stock_dict["symbol"]}""" for stock_dict in get_stock_names(auth_key)]

def post_transaction(auth_key: str, symbol: str, amount: int, transaction_type: str):
    json = {"symbol": symbol,
            "amount": amount,
            "transactionType": transaction_type}
    return requests.post(BASE_URL + "portfolio/transaction", headers={"api_key": auth_key}, json=json)

def get_stock_description(auth_key: str, symbol: str):
    return requests.get(BASE_URL + f"stock/{symbol}/description", headers={"api_key": auth_key}).json()


def get_stockprice_history(auth_key: str, symbol: str, period: str):
    return requests.get(BASE_URL + f"stock/{symbol}/history?period={period}", headers={"api_key": auth_key}).json()

def get_user_transaction_fee(auth_key: str):
    return requests.get(BASE_URL + "user/settings", headers={"api_key": auth_key}).json()

@st.cache(show_spinner=False)
def get_user_portfolio(auth_key: str):
    return requests.get(BASE_URL + "portfolio", headers={"api_key": auth_key}).json()

def delete_user(auth_key: str):
    return requests.delete(BASE_URL + "user/TEST", headers={"api_key": auth_key}).json()

def post_settings(auth_key:str, transactionFee: float):
    json = {"transactionFee": transactionFee}
    return requests.post(BASE_URL + "user/settings", headers={"api_key": auth_key}, json=json)

def get_sustainability_info(auth_key: str, symbol: str):
    return requests.get(BASE_URL + f"stock/{symbol}/sustainability", headers={"api_key":auth_key}).json()