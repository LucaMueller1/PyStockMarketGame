import utilities.requests_server as requests_server
import streamlit as st


def delete_user(auth_key):
    requests_server.delete_user(auth_key)

