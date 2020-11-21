import utilities.requests_server as requests_server
import streamlit as st
import pandas

"""
    desc: Creates FrontEnd page page for the sell portion of the broker page using the Streamlit framework.

    author: Luca Weissbeck

    date: 2020-10-14
"""


def delete_user(auth_key):
    requests_server.delete_user(auth_key)


def post_new_transaction_fees(auth_key, transaction_fee):
    requests_server.post_settings(auth_key, transaction_fee)


def get_transaction_fees(auth_key):
    transaction_fees = (requests_server.get_user_transaction_fee(auth_key))[
        "transactionFee"
    ]
    return transaction_fees

def write_sustainability_warning():
    st.header("Possible Sustainability Warnings️")
    st.write("🍺Alcoholic Beverages")
    st.write("🔞Adult Entertainment")
    st.write("🎰Gambling")
    st.write("🚬Tobacco Products")
    st.write("🐒Animal Testing")
    st.write("🐮Fur and Specialty Leather")
    st.write("💣Controversial Weapons")
    st.write("🔫Small Arms")
    st.write("🧪Catholic Values (Flags a company's involvement in abortion, contraceptives or human embryonic stem cell and fetal tissue research)")
    st.write("🌽Genetically Modified Organism (GMO)")
    st.write("🎖Military Contracting")
    st.write("☠️Pesticides")
    st.write("🏭Thermal Coal")
    st.write("🌴Palm Oil")

