from swagger_server.services.db_service import DatabaseConn
from swagger_server.models.portfolio_position import PortfolioPosition
from swagger_server.models.user import User
from swagger_server.services.finance import finance_data
from swagger_server.models.auth_key import AuthKey
from swagger_server.models.stock_description import StockDescription
from swagger_server.services.finance import finance_data
from swagger_server.models.api_error import ApiError
from swagger_server.models.transaction import Transaction
from swagger_server.controllers import staticglobaldb
import time
import re

deadlock = False # might be used in the future to prevent simultaneous buying and selling

def buy_stocks(auth_key: AuthKey, stock_description: StockDescription, amount: int):
    """
    buy_stock is being called when there are stocks being bought. It checks if there is
    enough money available for the transaction the user wants to make and creates a
    transaction with the current stock_price and transaction_fee

    :author: Jannik Sinz <jannik.sinz@ibm.com>
    :date: '06-11-2020'

    :param auth_key: auth key for the user meant to make the transaction
    :param stock_description: might only need a StockDescription object with the symbol
    :param amount: amount of stocks being bought
    :return: Transaction - to check for mistakes
            ApiError - in case of insufficient funds
    :test: create a transaction and check if the returned transaction has all the right values
    """

    conn = DatabaseConn()
    # is there enough money
    user = conn.get_user_by_auth_key(auth_key)
    money_avaiable = user.money_available

    # if stock_price already in stock_prices table:
    stock_value = finance_data.check_current_stock_price(stock_description)
    purchase_value = stock_value.stock_price * amount

    # check money available?
    if purchase_value <= money_avaiable:
        # lock access to buying, selling (security)

        # DEADLOCK
        """ deadlock = "buy"
        # validate lock
        # if deadlock != "buy"
        #     time.sleep(0.2)
        #     buy_stock(auth_key, stock_description, amount)
        #     break
        # else:
            # do stuff
                # create transaction - insert
            # remove lock
            # deadlock = False
        """

        # create Transaction
        settings = conn.get_settings_by_user(user)
        transaction_fee = settings.transaction_fee
        transaction = Transaction(None, stock_value, amount, "buy", transaction_fee)
        # buy stocks (insert transaction)
        conn.insert_transaction(transaction)
        return transaction
    else:
        return ApiError(detail="Not enough money available for this transaction", status=400, title="Insufficient Cash", type="/portfolio/transaction")


def sell_stocks(auth_key: AuthKey, stock_description: StockDescription, amount: int):
    """
    sell_stock is being called when there are stocks being sold. It checks if there are
    enough stocks owned for the transaction the user wants to make and creates a
    transaction with the current stock_price and transaction_fee

    :author: Jannik Sinz <jannik.sinz@ibm.com>
    :date: '06-11-2020'

    :param auth_key: auth key for the user meant to make the transaction
    :param stock_description: might only need a StockDescription object with the symbol
    :param amount: amount of stocks being bought
    :return: Transaction - to check for mistakes
            ApiError - in case of insufficient stocks owned
    :test: create a transaction and check if the returned transaction has all the right values

    """
    conn = DatabaseConn()
    user = conn.get_user_by_auth_key(auth_key)

    # check for stock price:
    stock_value = finance_data.check_current_stock_price(stock_description) # gets current StockValue
    purchase_value = stock_value.stock_price * amount # gets price from StockValue * amount

    # are there enough stocks owned ?
    portfolio_positions = stock_values_available(user)

    # iterate trhough PortfolioPositions for position.symbol = stock_description.symbol
    stock = None
    for position in portfolio_positions:
        if position.symbol == stock_description.symbol:
            stock = position

    amount_owned = stock.amount

    if amount <= amount_owned:
        # success !!!!
        # lock access to buying, selling (security)
        # DEADLOCK
        """ deadlock = "buy"
        # validate lock
        # if deadlock != "buy"
        #     time.sleep(0.2)
        #     buy_stock(auth_key, stock_description, amount)
        #     break
        # else:
            # do stuff
                # create transaction - insert
            # remove lock
            # deadlock = False
        """

        # create Transaction
        settings = conn.get_settings_by_user(user)
        transaction_fee = settings.transaction_fee
        transaction = Transaction(None, stock_value, amount, "sell", transaction_fee)
        # buy stocks (insert transaction)
        conn.insert_transaction(transaction)
        return transaction
    else:
        # not enough stocks owned
        return ApiError(detail="Not enough stocks owned for this transaction", status=400, title="Insufficient stocks", type="/portfolio/transaction")


def stock_values_available(user: User):
    """ stock_values_available is a smaller version of get_portfolio_positions.
        It only calculates the current amount of stocks owned and the corresponding symbol

        !!! This does not return a complete PortfolioPosition !!!

    :author: Jannik Sinz <jannik.sinz@ibm.com>
    :date: 05.11.2020
    :param user: provides the user of which the transaction will be pulled from the db
    :return: List of PortfolioPositions w/ only the current amount and the symbol
    :test: try to sell more stocks than you own. If it fails this function caught you cheating ;)
    """
    conn = DatabaseConn()
    transactions = conn.get_transactions_and_stock_by_user(user)

    stocks = []
    for transaction in transactions:
        symbol = transaction[1].symbol
        next_amount = transaction[0].amount
        transaction_type = transaction[0].transaction_type

        symbol_index = None
        found = False
        for i in range(len(stocks)):
            if stocks[i].symbol == symbol:
                found = True
                symbol_index = i
                break

        if not found:
            stocks.append(PortfolioPosition(symbol, None, next_amount, None, None))
        else:
            # get Portfoliopostition out of list
            prev_position = stocks[symbol_index]  # 5 Stocks 120€ + 5€

            if transaction_type == "buy":
                prev_position.amount += next_amount     # 5   + 3   = 8stk
            else:
                prev_position.amount -= next_amount

            #new Buy-In price (division by zero)
            if prev_position.amount <= 0:
                stocks[symbol_index] = None
                stocks.pop(symbol_index)
            else:
                # override PortfolioPosition
                stocks[symbol_index] = prev_position

    return stocks


def get_portfolio_positions(user: User):
    """ !!! this does not calculate the history of the depot !!! -> get_portfolio_history

        get_portfolio_positions creates a PortfolioPosition for every Stock that has been bought or sold
        in the past.
        it checks through every transaction made in the past and calculates the average
        Buy-In price as well as the current amount of stocks owned.

    :author: Jannik Sinz <jannik.sinz@ibm.com>
    :date: 05.11.2020
    :param user: current user
    :return: Array of PortfolioPositions
    :test: make some transactions and go to the portfolio site of the stock. Amount and Buy-In
            price should be equal to what you bought/sold
    """
    # get all stock transactions
    # conn = DatabaseConn()
    transactions = staticglobaldb.dbconn.get_transactions_and_stock_by_user(user)
    # print(transactions)

    # for every symbol
    stocks = []
    for transaction in transactions:
        symbol = transaction[1].symbol #AAPL
        stock_name = transaction[1].stock_name # Apple
        logo_url = transaction[1].logo_url
        next_amount = transaction[0].amount # 5
        transaction_fee = transaction[0].transaction_fee # 10€
        next_stock_buyin_price = transaction[0].stock_value.stock_price + (transaction_fee/next_amount) # price at buy with fee
        transaction_type = transaction[0].transaction_type


        symbol_index = None
        found = False
        for i in range(len(stocks)):
            if stocks[i].symbol == symbol:
                found = True
                symbol_index = i
                break

        if not found:
            stocks.append(PortfolioPosition(symbol=symbol, stock_name=stock_name, logo_url=logo_url, amount=next_amount, stock_value=None, stock_buyin_price=next_stock_buyin_price))
        else:
            # get PortfolioPostition out of list
            prev_transaction = stocks[symbol_index] # 5 Aktien 120€ + 5€


            # Buy-In/Amount calculation
            prev_value = prev_transaction.amount * prev_transaction.stock_buyin_price # 5*120 = 600 + 5€ = 605€
            next_value = next_amount * next_stock_buyin_price # 3*95€ + 5€ = 290€

            if transaction_type == "buy":
                prev_value += next_value                # 605 + 290 = 895€
                prev_transaction.amount += next_amount     # 5   + 3   = 8stk
            else:
                prev_value -= next_value
                prev_transaction.amount -= next_amount

            #new Buy-In price (division by zero)
            if prev_transaction.amount <= 0:
                stocks[symbol_index] = None
                stocks.pop(symbol_index)
            else:
                prev_transaction.stock_buyin_price = prev_value/prev_transaction.amount # 895€ / 8stk
                # override PortfolioPosition
                stocks[symbol_index] = prev_transaction

    for index in range(len(stocks)):  # Moved insertion of current stock prices here to exclude stocks that are completely sold already
        if stocks[index].stock_value is None:
            current_stock_price = staticglobaldb.dbconn.get_stock_price_from_today(symbol)
            if current_stock_price is None:
                current_stock_price = finance_data.insert_stock_history_from_yfinance_to_db(symbol, "1d")
            stocks[index].stock_value = current_stock_price

    return stocks


def get_portfolio_history(user: User, days: int):
    """ Gives History of whole Portfolio for use in a graph

    :param user:
    :return: array of PortfolioValue
    """
    current_depot_value = None

    for day in range(days):

        portfolio_array = get_portfolio_positions(user)
        print(portfolio_array)

    pass


# user = User(2, "Luca", "Weissbeck", "lucaweissbeck@yahoo.de", "$2b$12$.7atD7IuL.LH0/XbGONOiu3l6aJ2Ux/1r2/ExWIsJYukcymy8181C", 10000, 10000)
# stock_portfolio_position(user)
# data = get_portfolio_positions(user)
# print(data)
# get_portfolio_history(user, 1)