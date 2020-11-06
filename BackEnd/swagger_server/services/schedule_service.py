import schedule
import time
from swagger_server.services.finance import finance_data
from swagger_server.services import trading_service
from swagger_server.services.db_service import DatabaseConn


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
            schedule.every(24).hour.do(finance_data.insert_stock_history_from_yfinance_to_db(symbol))

