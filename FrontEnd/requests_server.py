import requests

BASE_URL = "http://localhost:8080/api/"

def login(user_name_input: str, password_input: str) -> requests.Response:
    json = {'email': user_name_input,
            'password': password_input}

    return requests.post(BASE_URL + "user/login", json=json)

def get_stock_names(auth_key: str) -> requests.Response:
    return requests.get(BASE_URL + "stock", headers={"api_key":auth_key})
