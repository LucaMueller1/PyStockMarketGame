import streamlit as st
from html_table_generator import PortfolioTable
import side_bar
import chart_generator
import requests_server

data = [
  {
    "symbol": "AAA",
    "logoUrl": "https://images-ext-1.discordapp.net/external/clYzqjuQDH7RDXkxdcEgIAvbL2soZpZHsoGfztBj6wQ/https/logo.clearbit.com/adidas-group.com",
    "stockName": "AAA",
    "amount": 5,
    "stock_price": 3.13,
    "stock_buyin_price": 2,
    "countryId": "Germany",
    "industry": "STONKS"
  },
  {
    "symbol": "BBB",
    "logoUrl": "https://dlskits.com/wp-content/uploads/2018/05/512x512-Logo-Juventus-for-Dream-League-Soccer.png",
    "stockName": "Juve",
    "amount": 2,
    "stock_price": 1.11,
    "stock_buyin_price": 2.22,
    "countryId": "England",
    "industry": "Military"
  }
]

def run(session_state):

    st.title("Portfolio")
    st.write("Hallo Ben Dover")

    chart_generator.show_chart()

    html_table = PortfolioTable()
    html_table.open()
    html_table.add_headers()
    html_table.add_portfolio(data)
    html_table.close()

    st.markdown(html_table.get_html(), unsafe_allow_html=True)

    side_bar.run(session_state)