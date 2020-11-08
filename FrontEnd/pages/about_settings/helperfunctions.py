import utilities.requests_server as requests_server
import streamlit as st


def delete_user(auth_key):
    requests_server.delete_user(auth_key)

def post_new_transaction_fees(auth_key, transaction_fee):
    requests_server.post_settings(auth_key, transaction_fee)