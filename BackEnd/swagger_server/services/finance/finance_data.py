import yfinance as yf
import pandas as pd

from swagger_server.models import StockValue, StockDescription, StockSustainability
from swagger_server.services.db_service import DatabaseConn
from swagger_server.controllers import staticglobaldb
import datetime

"""

"""
# print(staticglobaldb.dbconn.get_transactions_and_stock_by_user(User(id=3)))

# stocks = (
# "ADS.DE", "ALV.DE", "BAS.DE", "BAYN.DE", "BEI.DE", "BMW.DE", "CON.DE", "1COV.DE", "DAI.DE", "DHER.DE", "DKB.DE",
# "DB1.DE", "DPW.DE", "DTE.DE", "DWNI.DE", "EOAN.DE", "FRE.DE", "FME.DE", "HEI.DE", "HEN3.DE", "IFX.DE", "LIN.DE",
# "MRK.DE", "MTX.DE", "MUV2.DE", "RWE.DE", "SAP.DE", "SIE.DE", "VOW3.DE", "VNA.DE")

def check_current_stock_price(stock_description: StockDescription):
    """
    check_current_stock_price is a helper function that calls the DB and
    checks if there is a price for the stock_description.symbol for today.
    If ther is none it will call the current stock_price from the yfinance
    api.

    :param StockDescription: it might only need the symbol attribute set in the StockDescription Model
    :return: StockValue - with the current stock_price
    """
    stock_symbol = stock_description.symbol
    stock_value = staticglobaldb.dbconn.get_stock_price_from_today(stock_symbol) # StockValue Model

    if stock_value is not None: # StockValue
        # get price for today
        stock_price = stock_value.stock_price # stock_price from StockValue
    else:
        # get it from API
        # + insert into table
        symbol = stock_description.symbol # Symbol from StockValue
        stock_value = insert_stock_history_from_yfinance_to_db(symbol, "1d") # StockValue Model
        # ^ this already calls the function insert_course for the DB

    return stock_value


def get_stock_price_for_date(stock_description: StockDescription, history_date: datetime):
    """
    get_stock_price_for_date is a helper function that calls the DB and
    checks if there is a price for the stock_description.symbol for the date provided.
    If ther is none it will call the current stock_price from the yfinance
    api.

    :param StockDescription: it might only need the symbol attribute set in the StockDescription Model
    :return: StockValue - with the current stock_price
    """
    today = datetime.datetime.now().date()
    stock_symbol = stock_description.symbol

    # making sure stock_value returnes valid data
    stock_value = 0
    if history_date != today:
        stock_value = staticglobaldb.dbconn.get_stock_price_from_date(stock_symbol, history_date) # StockValue Model
    else:
        stock_value = check_current_stock_price(stock_description)

    if stock_value is None: # StockValue
        # get price for today
        # stock_price = stock_value.stock_price # stock_price from StockValue
        # get it from API
        # + insert into table
        symbol = stock_description.symbol # Symbol from StockValue
        stock_value = insert_stock_history_from_yfinance_to_db(symbol, "1d") # StockValue Model
        # ^ this already calls the function insert_course for the DB

    return stock_value


def insert_stock_history_from_yfinance_to_db(symbol: str, period: str):
    """This function takes the symbol and period of a stock and sends the
        data as a StockValue model to the function DatabaseConn.insert_course()


    :param symbol: the ticker of the Stock
    :param period: The period of which the data is requested from the API
                (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
                re.sub(regex, string, replace)
    :return: StockValue

    """
    df = yf.Ticker(symbol).history(period)
    conn = DatabaseConn()

    value = None
    for index, row in df.iterrows():
        open_value = row['Open']
        if open_value is None or pd.isna(open_value):
            continue
        date = index
        value = StockValue(None, symbol, float(open_value), str(date))
        conn.insert_course(value)
    return value


def get_stock_history_to_frontend(symbol: str, period: str):
    """This function takes the symbol and period of a stock and sends the
        data as a StockValue model to the function DatabaseConn.insert_course()


    :param symbol: the ticker of the Stock
    :param period: The period of which the data is requested from the API
                (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
                re.sub(regex, string, replace)
    :return: StockValue

    """
    if symbol == "IBM":
        df = yf.Ticker(symbol).history(period)
        returned = []
        multiplier = 1
        for index, row in df.iterrows():
            open_value = row['Open']*multiplier
            if open_value is None or pd.isna(open_value):
                continue
            date = index
            returned.append(StockValue(None, symbol, float(open_value), str(date)))
            multiplier*1.1
        return returned # StockValue

    if symbol == "DDAIF":
        df = yf.Ticker(symbol).history(period)
        returned = []
        multiplier = 1
        for index, row in df.iterrows():
            open_value = row['Open']*multiplier
            if open_value is None or pd.isna(open_value):
                continue
            date = index
            returned.append(StockValue(None, symbol, float(open_value), str(date)))
            multiplier/1.1
        return returned # StockValue

    df = yf.Ticker(symbol).history(period)
    returned = []
    for index, row in df.iterrows():
        open_value = row['Open']
        if open_value is None or pd.isna(open_value):
            continue
        # close = row['Close']
        # high = row['High']
        # low = row['Low']
        date = index
        returned.append(StockValue(None, symbol, float(open_value), str(date)))
    return returned # StockValue


def get_stock_info_from_yfinance(symbol: str):
    """

    :param symbol:
    :return:
    """
    indexes = ["shortName", "country", "logo_url", "longBusinessSummary", "industry", "trailingAnnualDividendYield", "marketCap", "fiftyTwoWeekLow", "fiftyTwoWeekHigh", "fullTimeEmployees"]
    # indexes = StockDescription().__dict__.keys()

    info = yf.Ticker(symbol).info
    for value in info:
        if info[value] is None:
            info[value] = "N/A"

    for index in indexes:
        if index not in info:
            info[index] = "N/A"


    description = StockDescription(symbol, info['shortName'], info['country'], info['logo_url'], info['longBusinessSummary'], info['industry'], info['trailingAnnualDividendYield'], info['marketCap'], info['fiftyTwoWeekLow'], info['fiftyTwoWeekHigh'], info['fullTimeEmployees'])

    # print(description)
    conn = DatabaseConn()
    success = conn.update_stock(description)
    # print("Status: ", success)
    return description


def get_stock_sustainability(symbol: str):
    """

    :param symbol:
    :return:
    """
    sus = yf.Ticker(symbol).sustainability
    if sus is not None:
        sus = sus.to_dict()['Value']
        return sus
    else:
        return {}




#
#
# def get_stock_data_from_db(symbol: str, period: str):
#     print(symbol)
#     print(period)

#     pass
# insert_stock_history_from_yfinance_to_db("IBM", "1d")
# print(get_stock_info_from_yfinance("SBUX"))
# print(yf.Ticker("SBUX").info)
# print(get_stock_info_from_yfinance("SBUX"))