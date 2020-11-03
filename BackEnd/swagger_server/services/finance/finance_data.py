import yfinance as yf
import pandas as pd
import xlrd
import sqlalchemy as sqla

from swagger_server.models import StockValue, StockDescription
from swagger_server.models.user import User
from swagger_server.models.stock_search_result import StockSearchResult
from swagger_server.controllers import staticglobaldb
from swagger_server.services.db_service import DatabaseConn

"""

"""
# print(staticglobaldb.dbconn.get_transactions_and_stock_by_user(User(id=3)))

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

def get_stock_history_from_yfinance(symbol: str, period: str):
    """This function takes the symbol and period of a stock and sends the
        data as a StockValue model to the function DatabaseConn.insert_course()


    :param symbol: the ticker of the Stock
    :param period: The period of which the data is requested from the API
                (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
                re.sub(regex, string, replace)

    """
    stock = yf.Ticker(symbol)
    history = stock.history(period)

    day = 0
    for day in history:
        value = StockValue()
        conn = DatabaseConn()
        conn.insert_course(value)
        ++day
    pass


def get_stock_info_from_yfinance(symbol: str):
    """

    :param symbol:
    :return:
    """
    stock = yf.Ticker(symbol)
    info = stock.info
    description = StockDescription(symbol, info['shortName'], info['country'], info['logo_url'], info['longBusinessSummary'], info['industry'], info['trailingAnnualDividendYield'], info['marketCap'], info['fiftyTwoWeekLow'], info['fiftyTwoWeekHigh'], info['fullTimeEmployees'])
    print(description)
    conn = DatabaseConn()
    bool = conn.update_stock(description)
    return description

# get_stock_history_from_yfinance("IBM", "5d")


def __init__(self):
    return
