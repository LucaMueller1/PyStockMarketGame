from swagger_server.services.finance import finance_data
from swagger_server.services import trading_service
from swagger_server.services.db_service import DatabaseConn

import datetime

def InsertStockData():
    print("CronJob for inserting StockData started at: " + str(datetime.datetime.now()))




    """
    conn = DatabaseConn()
    users = conn.get_all_users()
    stocks = []

    for user in users:
        portfolio = trading_service.get_portfolio_positions(user)
        for position in portfolio:
            symbol = position.symbol
            # make sure double data is not collected
            if symbol not in stocks:
                stocks.append(symbol)

"""