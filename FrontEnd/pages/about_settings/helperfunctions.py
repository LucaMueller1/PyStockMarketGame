import utilities.requests_server as requests_server
import streamlit as st

"""
    desc: Creates FrontEnd page page for the sell portion of the broker page using the Streamlit framework.

    author: Luca Weissbeck

    date: 2020-10-14
"""


def delete_user(auth_key):
    """
    Calls method for API request in order to delete user.

    :param auth_key: (String) API key authorizing and identifying the user.
    :test Correct: Valid auth_key is supplied. Incorrect: No auth_key is supplied and API request fails.
    """
    requests_server.delete_user(auth_key)


def post_new_transaction_fees(auth_key, transaction_fee):
    """
    Calls method for API request in order to post updated transaction fees.

    :param auth_key: (String) API key authorizing and identifying the user.
    :param transaction_fee: (Float)
    :test Correct: Method is called using a valid auth_key and transaction_fee --> API request is successful. Incorrect: Method is called using an invalid auth_key leading to a failed API request.
    """
    requests_server.post_settings(auth_key, transaction_fee)


def get_transaction_fees(auth_key):
    """
    Gets the current transaction fees by calling the appropriate API request.

    :param auth_key: (String) API key authorizing and identifying the user.
    :return: (String)
    :test Correct: Method is called using a valid authkey which results in successful.
    """
    transaction_fees = (requests_server.get_user_transaction_fee(auth_key))[
        "transactionFee"
    ]
    return transaction_fees


