import yfinance as yf
import pandas as pd

from swagger_server.models import StockValue, StockDescription, StockSustainability
from swagger_server.services.db_service import DatabaseConn
from swagger_server.controllers import staticglobaldb
import datetime



def check_current_stock_price(symbol: str):
    """
    check_current_stock_price is a helper function that calls the DB and
    checks if there is a price for the stock_description.symbol for today.
    If ther is none it will call the current stock_price from the yfinance
    api.

    :author: Jannik Sinz <jannik.sinz@ibm.com>
    :date:

    :param StockDescription: it might only need the symbol attribute set in the StockDescription Model
    :return: StockValue - with the current stock_price
    """
    stock_symbol = symbol
    stock_value = staticglobaldb.dbconn.get_stock_price_from_today(stock_symbol) # StockValue Model

    if stock_value is not None: # StockValue
        # get price for today
        stock_price = stock_value.stock_price # stock_price from StockValue
    else:
        # get it from API
        # + insert into table
        symbol = symbol # Symbol from StockValue
        stock_value = insert_stock_history_from_yfinance_to_db(symbol, "1d") # StockValue Model
        # ^ this already calls the function insert_course for the DB

    return stock_value


def get_stock_price_for_date(stock_description: StockDescription, history_date: datetime):
    """
    get_stock_price_for_date is a helper function that calls the DB and
    checks if there is a price for the stock_description.symbol for the date provided.
    If ther is none it will call the current stock_price from the yfinance
    api.

    :author: Jannik Sinz <jannik.sinz@ibm.com>
    :date:

    :param StockDescription: it might only need the symbol attribute set in the StockDescription Model
    :return: StockValue - with the stock_price for date
    """
    stock_symbol = stock_description.symbol

    # making sure stock_value returnes valid data
    stock_value = 0


    stock_value = staticglobaldb.dbconn.get_stock_price_from_date(stock_symbol, history_date) # StockValue Model

    if stock_value is None: # StockValue

        symbol = stock_description.symbol # Symbol from StockValue
        stock_value = __insert_stock_history_for_date_to_db(symbol, history_date)
        # print("StockValue for ", history_date,": ", stock_value)

    return stock_value


def insert_stock_history_from_yfinance_to_db(symbol: str, period: str):
    """This function takes the symbol and period of a stock and sends the
        data as a StockValue model to the function DatabaseConn.insert_course()

    :author: Jannik Sinz <jannik.sinz@gmx.de>
    :date:


    :param symbol: the ticker of the Stock
    :param period: The period of which the data is requested from the API
                (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
                re.sub(regex, string, replace)
    :return: StockValue

    """
    df = yf.Ticker(symbol).history(period)

    value = None
    for date, row in df.iterrows():
        open_value = row['Open']
        if open_value is None or pd.isna(open_value):
            continue
        value = StockValue(None, symbol, float(open_value), str(date))
        staticglobaldb.dbconn.insert_course(value)
    return value


def __insert_stock_history_for_date_to_db(symbol: str, history_date: str):
    """This function takes the symbol and period of a stock and sends the
        data as a StockValue model to the function DatabaseConn.insert_course()

    :author: Jannik Sinz <jannik.sinz@ibm.com>
    :date:

    :param symbol: the ticker of the Stock
    :param period: The period of which the data is requested from the API
                (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
                re.sub(regex, string, replace)
    :return: StockValue

    """
    date += datetime.timedelta(days=1)
    start_date = history_date
    end_date = history_date

    # insure its always getting the last weekday
    df = yf.Ticker(symbol).history(start=start_date, end=start_date)

    value = None
    for index, row in df.iterrows():
        open_value = row['Open']
        if open_value is None or pd.isna(open_value):
            continue
        date = index
        value = StockValue(None, symbol, float(open_value), str(date))
        # print(value.stock_price)
        staticglobaldb.dbconn.insert_course(value)
    return value


def get_stock_history_to_frontend(symbol: str, period: str):
    """This function takes the symbol and period of a stock and sends the
        data as a StockValue model to the function DatabaseConn.insert_course()

    :author: Jannik Sinz <jannik.sinz@ibm.com>
    :date:


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
    get_stock_info_from_yfianace calls the yfinance Api and
    returns the info about the stock as a StockDescription object

    :author: Jannik Sinz <jannik.sinz@ibm.com>
    :date:

    :param symbol: the stock ticker
    :return: StockDescription
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
    success = staticglobaldb.dbconn.update_stock(description)
    # print("Status: ", success)
    return description


def get_stock_sustainability(symbol: str):
    """
    get_stock_sustainability calls the yfinance Api and returns
    gets controversial information the company has
    associations with. It then turns the information into a dict
    and returns it.

    :param symbol: ticker of the stock
    :return: dict
    """
    sus = yf.Ticker(symbol).sustainability
    if sus is not None:
        sus = sus.to_dict()['Value']
        return sus
    else:
        return {}


# print(get_stock_sustainability("IBM"))

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
# description = StockDescription(symbol="IBM")
# print(get_stock_price_for_date(description, '2020-11-02'))
# print(get_stock_price_for_date('2020-11-19'))
# print(yf.Ticker("IBM").history(start='2020-11-03', end='2020-11-03'))