from swagger_server.services.db_service import DatabaseConn
from swagger_server.models.portfolio_position import PortfolioPosition
from swagger_server.models.user import User
from swagger_server.models.auth_key import AuthKey
from swagger_server.models.stock_description import StockDescription
from swagger_server.models.api_error import ApiError
from swagger_server.models.transaction import Transaction
from swagger_server.controllers import staticglobaldb
from swagger_server.models.portfolio_value import PortfolioValue
from swagger_server.services.finance import finance_data
import swagger_server.services.schedule_service as schedule_service
from swagger_server.models.transaction_prepare import TransactionPrepare
from swagger_server.models.settings import Settings

import datetime
import re

# deadlock = False # might be used in the future to prevent simultaneous buying and selling


def buy_stocks(user: User, symbol: str, amount: int):
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

    # is there enough money
    money_available = user.money_available

    # to fetch users transaction fee
    settings: Settings = staticglobaldb.dbconn.get_settings_by_user(user)

    # if stock_price already in stock_prices table:
    stock_value = finance_data.check_current_stock_price(symbol)
    purchase_value = stock_value.stock_price * abs(amount) - abs(float(settings.transaction_fee))

    # check money available?
    if purchase_value <= money_available:
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

        # create TransactionPrepare
        transaction_prepare = TransactionPrepare(symbol, abs(amount), "buy")

        # buy stocks (insert transaction)
        transaction = staticglobaldb.dbconn.insert_transaction(transaction_prepare, user)

        # calculate new_portfolio_cash & update user
        new_portfolio_cash = user.money_available - (transaction.stock_value.stock_price * abs(amount)) - abs(float(settings.transaction_fee))
        user.money_available = new_portfolio_cash
        staticglobaldb.dbconn.update_user(user)
        return transaction
    else:
        return None


def sell_stocks(user: User, symbol: str, amount: int):
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

    # check for stock price:
    stock_value = finance_data.check_current_stock_price(symbol) # gets current StockValue

    purchase_value = stock_value.stock_price * amount # gets price from StockValue * amount

    # to fetch users transaction fee
    settings: Settings = staticglobaldb.dbconn.get_settings_by_user(user)

    # are there enough stocks owned ?
    portfolio_positions = stock_values_available(user)

    # iterate through PortfolioPositions for position.symbol = stock_description.symbol
    stock = None
    for position in portfolio_positions:
        if position.symbol == symbol:
            stock = position

    amount_owned = stock.amount

    if amount <= amount_owned:
        # success !!!!
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

        # create TransactionPrepare
        transaction_prepare = TransactionPrepare(symbol, amount, "sell")
        # sell stocks (insert transaction)
        transaction = staticglobaldb.dbconn.insert_transaction(transaction_prepare, user)

        # calculate new_portfolio_cash & update user
        new_portfolio_cash = user.money_available + (transaction.stock_value.stock_price * abs(amount)) - abs(float(settings.transaction_fee))
        user.money_available = new_portfolio_cash
        staticglobaldb.dbconn.update_user(user)

        return transaction
    else:
        return None


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
            stocks.append(PortfolioPosition(symbol=symbol, stock_name=None, logo_url=None, amount=next_amount, stock_value=None, stock_buyin_price=None))
        else:
            # get Portfoliopostition out of list
            prev_position = stocks[symbol_index]  # 5 Stocks 120€ + 5€

            if transaction_type == "buy":
                prev_position.amount += next_amount     # 5   + 3   = 8stk
            else:
                prev_position.amount -= next_amount

            # new Buy-In price (division by zero)
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

    stocks = remove_sold_stocks(stocks)

    return stocks


def get_portfolio_history(user: User):
    """ Gives History of whole Portfolio for one User for use in a graph.
        get_portfolio_history takes the user as input and gets all the users
        transactions from the DB. For each day since the first trade it goes
        through the transactions and creates/updates PortfolioPositions.
        Based on the positions it calculates it into a PortfolioValue for
        each day.

    :author: Jannik Sinz <jannik.sinz@ibm.com>
    :date: 12.11.2020
    :param user: the User from which the PortfolioValues (History) should be returned
    :return: List[PortfolioValue]
    :test: provide a user as input. You should receive a list of PortfolioValues
    """

    # get all stock transactions
    transactions = staticglobaldb.dbconn.get_transactions_and_stock_by_user(user)
    # get first trading day
    min_date = get_min_date(transactions) # datetime
    # print("Min-Date: ",min_date)
    last_portfolio_value = 0
    # start_date = min_date + datetime.timedelta(days=-1)
    # print(start_date)

    """
    Create PortfolioValues for specific dates
    """
    now = datetime.datetime.now().date()
    date = min_date

    stocks = []
    returned = [] # list of PortfolioValue
    # while date <= now
    while date <= now:
        # print("working_date: ", date)
        # print("Today is the: ", now)
        # for every transaction

        # transactions = staticglobaldb.dbconn.get_transactions_and_stock_by_user(user)
        for transaction in transactions:
            # print("Transactions on: ", date, ": ", len(transactions))
            # get values
            symbol = transaction[1].symbol #AAPL
            stock_name = transaction[1].stock_name # Apple
            logo_url = transaction[1].logo_url
            next_amount = transaction[0].amount # 5
            transaction_fee = transaction[0].transaction_fee # 10€
            next_stock_buyin_price = transaction[0].stock_value.stock_price + (transaction_fee/next_amount) # price at buy with fee
            transaction_type = transaction[0].transaction_type
            transaction_date = transaction[0].stock_value.timestamp.date()

            # take transactions from date and add to PortfolioPositions
            # or create PortfolioPositions for the date
            if transaction_date == date:
                # print("Transaction found for ", date, "! It is: ", symbol)

                # check if portfolio is already in stocks
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
                    # update PortfolioPosition
                    prev_transaction = stocks[symbol_index]

                    """ Buy-In/Amount calculation """
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

                # add PortfolioValue to list
            # END IF date = transaction_date
        #END FOR - Transactions
        stocks = remove_sold_stocks(stocks)

        current_depot_value = 0
        # get stock_price for date
        for stock in stocks:
            d_stock_symbol = stock.symbol
            d_stock_amount = stock.amount
            d_stock_description = StockDescription(symbol=d_stock_symbol)
            d_stock_price = finance_data.get_stock_price_for_date(d_stock_description, date).stock_price
            current_depot_value += d_stock_price * d_stock_amount
            # print(d_stock_symbol, " on ", date, ": ", d_stock_price, "Amount: ", d_stock_amount)
            # print("DepotValue: ", current_depot_value)
        cash = user.money_available
        current_depot_value += cash

        # portfolio_Value
        portfolio_value = PortfolioValue(current_depot_value, date)
        returned.append(portfolio_value)
        date += datetime.timedelta(days=1)
        # print("PortfolioValue for ", date, ": ", portfolio_value)

    # END WHILE day = now
    # print("PortfolioValues: ", returned)
    return returned


## Support functions Portfolio
def remove_sold_stocks(stocks: list) -> list:
    """
    remove_sold_Stocks checks if a PortfolioPosition has a stock_value of zero
    and removes the PortfolioPosition from the list

    :param stocks: list() of PortfolioPositions
    :return: list() of PortfolioPositions
    """
    for index in range(len(stocks)):  # Moved insertion of current stock prices here to exclude stocks that are completely sold already
        if stocks[index].stock_value is None:
            # today's quotation from db
            current_stock_price = staticglobaldb.dbconn.get_stock_price_from_today(stocks[index].symbol)
            if current_stock_price is None:
                if not schedule_service.is_market_open():
                    # latest quotation from db
                    current_stock_price = staticglobaldb.dbconn.get_latest_stock_price(stocks[index].symbol)
                else:
                    # yFinance quotation
                    current_stock_price = finance_data.insert_stock_history_from_yfinance_to_db(stocks[index].symbol, "1d")
            stocks[index].stock_value = current_stock_price

    return stocks

def get_min_date(transactions: list) -> datetime:
    min_date = None
    for transaction in transactions:
        current_date = transaction[0].stock_value.timestamp.date()
        if min_date == None:
            min_date = current_date
        elif current_date < min_date:
            min_date = current_date

    return min_date
## End Support functions

def get_portfolio_analytics():
    pass


# user = staticglobaldb.dbconn.get_user_by_auth_key("zwsKmSFc64qqcK2TykZRasrOHk5JK4d7TRHZYCAjshuaXIuDJUeOqIA4TaL3PlDCryJid7HutJOmzH0sEenWh5YDfsI3J0UzQ2zzKdwV7KE08pFhu99i9P2ysLXZnm13")
# print(buy_stocks(user, "IBM", 1))
#
# print(user.first_name, user.last_name)
# history = get_portfolio_history(user)
# print(history)
# history = staticglobaldb.dbconn.get_stock_price_from_date()
# print(get_portfolio_positions(user))
