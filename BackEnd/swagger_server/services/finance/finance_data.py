import yfinance as yf
import pandas as pd
import xlrd
import sqlalchemy as sqla
from swagger_server.models.user import User
from swagger_server.models.stock_search_result import StockSearchResult
from swagger_server.controllers import staticglobaldb

"""

"""
print(staticglobaldb.dbconn.get_transactions_and_stock_by_user(User(id=3)))
stocks = (
"ADS.DE", "ALV.DE", "BAS.DE", "BAYN.DE", "BEI.DE", "BMW.DE", "CON.DE", "1COV.DE", "DAI.DE", "DHER.DE", "DKB.DE",
"DB1.DE", "DPW.DE", "DTE.DE", "DWNI.DE", "EOAN.DE", "FRE.DE", "FME.DE", "HEI.DE", "HEN3.DE", "IFX.DE", "LIN.DE",
"MRK.DE", "MTX.DE", "MUV2.DE", "RWE.DE", "SAP.DE", "SIE.DE", "VOW3.DE", "VNA.DE")

def get_tradable_values():
    df = pd.read_excel(r'data/traded_companies.xlsx')
    print(df)
    i = 0
    for line in df:
        try:
            stock_info = yf.Ticker(line[0])
            ++i
        except:
            print(line[0], f" 333 error retrieving %s from yfinance")
            ++i
            pd[i]

def get_stock_history_from_yfinance(symbol: str):
    stock = yf.Ticker(symbol)
    print(stock.info)
    print(stock.history("2d"))
    print("-------------")

    for day in stock.history(0):
        insert_stock_data()


def __init__(self):
    return
