import yfinance as yf
import pandas as pd
import xlrd
import sqlalchemy as sqla
import datetime

from swagger_server.models import StockValue, StockDescription
from swagger_server.models.user import User
from swagger_server.models.stock_search_result import StockSearchResult
from swagger_server.controllers import staticglobaldb
from swagger_server.services.db_service import DatabaseConn

"""

"""
# print(staticglobaldb.dbconn.get_transactions_and_stock_by_user(User(id=3)))

# stocks = (
# "ADS.DE", "ALV.DE", "BAS.DE", "BAYN.DE", "BEI.DE", "BMW.DE", "CON.DE", "1COV.DE", "DAI.DE", "DHER.DE", "DKB.DE",
# "DB1.DE", "DPW.DE", "DTE.DE", "DWNI.DE", "EOAN.DE", "FRE.DE", "FME.DE", "HEI.DE", "HEN3.DE", "IFX.DE", "LIN.DE",
# "MRK.DE", "MTX.DE", "MUV2.DE", "RWE.DE", "SAP.DE", "SIE.DE", "VOW3.DE", "VNA.DE")


def get_stock_history_from_yfinance(symbol: str, period: str):
    """This function takes the symbol and period of a stock and sends the
        data as a StockValue model to the function DatabaseConn.insert_course()


    :param symbol: the ticker of the Stock
    :param period: The period of which the data is requested from the API
                (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
                re.sub(regex, string, replace)

    """
    df = yf.Ticker(symbol).history(period)
    print(df)
    time = 0
    for index, row in df.iterrows():
        print(row.iloc)
        open = row['Open']

        value = StockValue(None, symbol, open, None)


def get_stock_data_from_db(symbol: str, period: str):

    pass


def get_stock_info_from_yfinance(symbol: str):
    """

    :param symbol:
    :return:
    """
    stock = yf.Ticker(symbol)
    info = stock.info
    for i in info:
        if info[i] is None:
            info[i] = "N/A"

    description = StockDescription(symbol, info['shortName'], info['country'], info['logo_url'], info['longBusinessSummary'], info['industry'], info['trailingAnnualDividendYield'], info['marketCap'], info['fiftyTwoWeekLow'], info['fiftyTwoWeekHigh'], info['fullTimeEmployees'])

    print(description)
    conn = DatabaseConn()
    success = conn.update_stock(description)
    print("Status: ", success)
    return description


# get_stock_history_from_yfinance("IBM", "5d")
