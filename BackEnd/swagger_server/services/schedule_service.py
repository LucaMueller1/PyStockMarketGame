from swagger_server.controllers import staticglobaldb
from swagger_server.services.finance import finance_data

import pandas_market_calendars as mcal
import pandas as pd
import datetime

"""

    desc: Handles the periodic insert of Stock values into the database

    author: Daniel Ebert

    date: 2020-11-09

"""


def insert_stock_data():
    """
        desc: Function that is periodically called every 15 minutes. Checks if the stock market is open and if yes, retrieves and inserts the course for every stock present in the transactions table if a course is missing for today into the database

        :author: Daniel Ebert <daniel.ebert@ibm.com>
        :date: 20.11.2020

        param: None

    """
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
    """
    desc: Helper function that returns a boolean containing the information whether the New York stock market is opened or closed. Beware: Timezone is forced with Europe/Berlin

    :author: Daniel Ebert <daniel.ebert@ibm.com>
    :date: 20.11.2020

    :return: True, False
    test: Correct: Call the function when you can ensure that the New York stock market is opened. Should return true. Incorrect: Function returns true when the NY stock market is closed/ false when it is opened
    """
    nyse_market_time = mcal.get_calendar('NYSE')
    start_time = datetime.datetime.now() - datetime.timedelta(days=1)
    end_time = datetime.datetime.now() + datetime.timedelta(days=1)
    early = nyse_market_time.schedule(start_date=start_time, end_date=end_time)
    is_open = nyse_market_time.open_at_time(early, pd.Timestamp(datetime.datetime.now(), tz="Europe/Berlin"))
    return is_open
