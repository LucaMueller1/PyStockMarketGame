import pandas as pd
from swagger_server.services.db_service import *
from swagger_server.models.portfolio_position import PortfolioPosition
from swagger_server.models.stock_value import StockValue

def buy_stock(symbol: str, anzahl: int):
    # is there enough money
    # lock access to buying, selling (security)
    # buy stocks

    return True


def stock_values_available(symbol: str, anzahl: int):

    # get amount owned
    # check if anzahl >= amount owned
    pass
    return True


def calculate_depot_money():
    pass
    return

def stock_portfolio_position(user: User):
    symbol = None; stock_name = None; amount = None; stock_value = None; StockValue = None; stock_buyin_price = None; logo_url = None
    


    portfolio_list = list().append(PortfolioPosition(symbol, stock_name, amount, stock_value, StockValue, stock_buyin_price, logo_url))
    return portfolio_list

