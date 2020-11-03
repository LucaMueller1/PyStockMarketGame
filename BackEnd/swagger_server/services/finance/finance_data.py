import yfinance as yf

from swagger_server.models import StockValue, StockDescription
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
    conn = DatabaseConn()

    for index, row in df.iterrows():
        open_value = row['Open']
        if open_value is None:
            continue
        # close = row['Close']
        # high = row['High']
        # low = row['Low']
        date = index
        value = StockValue(None, symbol, int(open_value), str(date))
        conn.insert_course(value)


@TypeError
def get_stock_history_to_frontend(symbol: str, period: str):
    """This function takes the symbol and period of a stock and sends the
        data as a StockValue model to the function DatabaseConn.insert_course()


    :param symbol: the ticker of the Stock
    :param period: The period of which the data is requested from the API
                (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
                re.sub(regex, string, replace)

    """
    df = yf.Ticker(symbol).history(period)
    returned = []
    for index, row in df.iterrows():
        open_value = row['Open']
        if open_value is None:
            continue
        date = index
        returned.append(StockValue(None, symbol, int(open_value), str(date)))
    return returned


def get_stock_data_from_db(symbol: str, period: str):
    print(symbol)
    print(period)
    pass


def get_stock_info_from_yfinance(symbol: str):
    """

    :param symbol:
    :return:
    """
    info = yf.Ticker(symbol).info
    for i in info:
        if info[i] is None:
            info[i] = "N/A"

    description = StockDescription(symbol, info['shortName'], info['country'], info['logo_url'], info['longBusinessSummary'], info['industry'], info['trailingAnnualDividendYield'], info['marketCap'], info['fiftyTwoWeekLow'], info['fiftyTwoWeekHigh'], info['fullTimeEmployees'])

    print(description)
    conn = DatabaseConn()
    success = conn.update_stock(description)
    print("Status: ", success)
    return description


get_stock_history_from_yfinance("IBM", "1d")
