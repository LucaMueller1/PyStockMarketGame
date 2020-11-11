from swagger_server.services.finance import finance_data
from swagger_server.services import trading_service
from swagger_server.services.db_service import DatabaseConn

import pandas_market_calendars as mcal
import pandas as pd
import datetime

def InsertStockData():
    print("CronJob for inserting StockData started at: " + str(datetime.datetime.now()))
    nyse_market_time = mcal.get_calendar('NYSE')
    start_time = datetime.datetime.now() - datetime.timedelta(days=1)
    end_time = datetime.datetime.now() + datetime.timedelta(days=1)
    early = nyse_market_time.schedule(start_date=start_time, end_date=end_time)
    is_open = nyse_market_time.open_at_time(early, pd.Timestamp(datetime.datetime.now(), tz="Europe/Berlin"))
    print("Is stock market open:", is_open)

def util_format_datetime_for_expiry(self, weeks: int) -> str:
    now = datetime.now()
    # result = now + relativedelta(weeks=weeks)
    # result = result.strftime('%Y-%m-%d %H:%M:%S')
   #  return result



InsertStockData()