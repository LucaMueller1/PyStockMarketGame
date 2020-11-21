import yfinance as yf
import pandas as pd
import datetime
from swagger_server.services.finance import finance_data
from swagger_server.services import db_service
from swagger_server.controllers import staticglobaldb
from swagger_server.models.stock_value import StockValue

def insert_one_month_courses():
    stocks = staticglobaldb.dbconn.get_all_stocks_distinct_in_transactions()
    print(stocks)
    today = datetime.datetime.now().date()
    print(today)
    for stock in stocks:
        symbol=stock
        df = pd.DataFrame()
        df = yf.Ticker('IBM').history(period="1mo")
        print(df)

        for index, row in df.iterrows():
            open_value = row['Open']
            if open_value is None or pd.isna(open_value):
                continue
            date = index
            value = StockValue(None, symbol, float(open_value), str(date))
            inserted = staticglobaldb.dbconn.insert_course(value)
            print(value)
            print(inserted)


insert_one_month_courses()