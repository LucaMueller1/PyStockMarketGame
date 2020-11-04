from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.transaction_prepare import TransactionPrepare  # noqa: E501
from swagger_server.models.user import User
from swagger_server.models.portfolio_position import PortfolioPosition
from swagger_server.services.db_service import DatabaseConn

user = User(2, "Luca", "Weissbeck", "lucaweissbeck@yahoo.de", "$2b$12$.7atD7IuL.LH0/XbGONOiu3l6aJ2Ux/1r2/ExWIsJYukcymy8181C", 10000, 10000)
conn = DatabaseConn()
transactions = conn.get_transactions_and_stock_by_user(user)
print(transactions)
posArr = list()

for i, item in enumerate(transactions):
    if i == 0:
        print(item[1].stock_name)
        # posArr.append(PortfolioPosition(item[1].symbol, item[1].stock_name, item[0].amount)
