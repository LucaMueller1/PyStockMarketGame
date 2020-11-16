from swagger_server.controllers import staticglobaldb
from swagger_server.services.finance import finance_data

import pandas_market_calendars as mcal
import pandas as pd
import datetime


def insert_stock_data():
    print("CronJob for inserting StockData started at: " + str(datetime.datetime.now()))
    is_open = is_market_open()
    print("Is stock market open:", is_open)

    if is_open:
        symbols = staticglobaldb.dbconn.get_all_stocks_distinct_in_transactions()
        for symbol in symbols:
            if staticglobaldb.dbconn.get_stock_price_from_today(symbol) is None:
                finance_data.insert_stock_history_from_yfinance_to_db(symbol, "1d")
                print("Inserting stock quotes for all users portfolio positions")


def is_market_open() -> bool:
    nyse_market_time = mcal.get_calendar('NYSE')
    start_time = datetime.datetime.now() - datetime.timedelta(days=1)
    end_time = datetime.datetime.now() + datetime.timedelta(days=1)
    early = nyse_market_time.schedule(start_date=start_time, end_date=end_time)
    is_open = nyse_market_time.open_at_time(early, pd.Timestamp(datetime.datetime.now(), tz="Europe/Berlin"))
    return is_open
