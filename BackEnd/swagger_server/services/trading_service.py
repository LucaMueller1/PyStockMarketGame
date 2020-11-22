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

import datetime
import re
import pandas as pd

# deadlock = False # might be used in the future to prevent simultaneous buying and selling


def buy_stocks(user: User, symbol: str, amount: int):
    """
    buy_stock is being called when there are stocks being bought. It checks if there is
    enough money available for the transaction the user wants to make and creates a
    TransactionPrepare object with the current stock_price and transaction_fee.

    It uses the inser_course function to insert the transaction and deducts
    the value + fees from the users account.

    :author: Jannik Sinz <jannik.sinz@ibm.com>
    :date: '06-11-2020'

    :param user: user meant to make the transaction
    :param symbol: symbol of the stock
    :param amount: amount of stocks being bought
    :return: Transaction - to check for mistakes
            None - in case of insufficient funds / unsuccessful purchase
    :test: create a transaction and check if the returned transaction has all the right values
    """

    # is there enough money
    money_avaiable = user.money_available
    settings = staticglobaldb.dbconn.get_settings_by_user(user)
    transaction_fee = settings.transaction_fee

    # if stock_price already in stock_prices table:
    stock_value = finance_data.check_current_stock_price(symbol)
    purchase_value = stock_value.stock_price * abs(amount) + transaction_fee

    # check money available?
    if purchase_value <= money_avaiable:
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

        # calculate new_depo_cash & update user
        user.money_available = user.money_available - (transaction.stock_value.stock_price * abs(amount)) - transaction_fee
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
    settings = staticglobaldb.dbconn.get_settings_by_user(user)
    transaction_fee = settings.transaction_fee

    purchase_value = stock_value.stock_price * amount + transaction_fee # gets price from StockValue * amount

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

        # calculate new_depo_cash & update user
        user.money_available = user.money_available + (transaction.stock_value.stock_price * abs(amount)) - transaction_fee
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
    transactions = staticglobaldb.dbconn.get_transactions_and_stock_by_user(user)

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


def get_portfolio_history_pandas(user: User):

    """Wir bekommen: Eine Liste aus Transactions(Symbol, amount, stockvalue(datetime, stock_price: float), transaction_type, transaction_fee: int)
        staticglobaldb.dbconn.get_transactions_and_stock_by_user(user)"""

    #staticglobaldb.dbconn.get_stock_price_from_date(symbol, datetime)

    transaction_and_info_list = staticglobaldb.dbconn.get_transactions_and_stock_by_user(user)
    # Verlauf PortfolioValue
    # DATE CASH VALUE

    daily_change_df = pd.DataFrame()

    date_list, change_list = __calculate_daily_cash_change(user, transaction_and_info_list)

    daily_change_df["date"] = date_list
    daily_change_df["change"] = change_list
    daily_change_df = daily_change_df.groupby(["date"]).sum()

    temp_cash_sum = user.starting_capital
    total_cash_per_day = []

    for index,row in daily_change_df.iterrows():
        temp_cash_sum += row.change
        total_cash_per_day.append(temp_cash_sum)

    daily_change_df["absolute_change"] = total_cash_per_day
    print("Total:", total_cash_per_day)

    portfolio_list, date_list = __calculate_daily_stock_change(user, transaction_and_info_list)

    stock_change_df = pd.DataFrame(columns=["symbol","amount","date","value","total_value"])

    for i, portfolio in enumerate(portfolio_list):
        stock_change_temp_df = pd.DataFrame(portfolio.items(), columns=["symbol","amount"])
        stock_change_temp_df["date"] = [date_list[i]] * len(stock_change_temp_df)
        stock_change_temp_df["value"] = stock_change_temp_df.apply(__get_value_for_postion, axis=1)
        stock_change_temp_df["total_value"] = stock_change_temp_df.apply(__get_daily_absolute_value, axis=1)
        stock_change_df = stock_change_df.append(stock_change_temp_df)
        stock_change_df = stock_change_df.dropna()
        stock_change_df = stock_change_df.groupby(["date"]).sum()
        
    
    
    return stock_change_df

    # finance_data.insert_stock_history_for_date_to_db(symbol, date)

def __get_value_for_postion(row: pd.Series):
    date = row.date
    date = date.to_pydatetime().date()

    return staticglobaldb.dbconn.get_stock_price_from_date(row.symbol, date)

def __get_daily_absolute_value(row: pd.Series):
    print(row.amount)
    print(row.value)
    print(row.date)
    if pd.isna(row.amount):
        return 0
    elif pd.isna(row.value):
        return None
    else:
        return row.amount * row.value.stock_price

def __calculate_daily_cash_change(user: User, transaction_and_info_list: list) -> tuple:

    date_list = []
    change_list = []

    # [(transaction, stock_search_result), ..., (transaction, stock_search_result)]
    for transaction_and_info in transaction_and_info_list:
        transaction = transaction_and_info[0]

        date_list.append(transaction.stock_value.timestamp)

        if transaction.transaction_type == "buy":
            change_list.append(-transaction.stock_value.stock_price * transaction.amount - transaction.transaction_fee)
        else:
            change_list.append(transaction.stock_value.stock_price * transaction.amount - transaction.transaction_fee)

    return (date_list, change_list)


def __calculate_daily_stock_change(user: User, transaction_and_info_list: list) -> pd.DataFrame:

    current_portfolio = {}

    portfolio_list = []
    date_list = []

    now = datetime.datetime.now()
    # print(transaction_and_info_list)
    date = get_min_date(transaction_list)
    while date <= now:
        for transaction in transaction_and_info_list:

                symbol = transaction[1].symbol #AAPL
                amount = transaction[0].amount # 5
                stock_value = transaction[0].stock_value.stock_price
                transaction_type = transaction[0].transaction_type
                transaction_date = transaction[0].stock_value.timestamp

                if transaction_date == date:
                    print("Transaction found for ", date, "! It is: ", symbol)

                    if symbol not in current_portfolio:
                        current_portfolio[symbol] = amount

                    elif transaction_type == "buy":
                        current_portfolio[symbol] = current_portfolio[symbol] + amount

                    else:
                        current_portfolio[symbol] = current_portfolio[symbol] - amount

        date_list.append(date)
        temp_portfolio = current_portfolio.copy()
        portfolio_list.append((temp_portfolio))
        date += datetime.timedelta(days=1)

    return (portfolio_list, date_list)


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
    capital = user.starting_capital
    print(min_date)

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
                print("Transaction found for ", date, "! It is: ", symbol)

                # check if portfolio is already in stocks
                symbol_index = None
                found = False
                for i in range(len(stocks)):
                    if stocks[i].symbol == symbol:
                        found = True
                        symbol_index = i
                        break

                # add PortfolioValue to list
                if not found:
                    print("new transaction insert")
                    stocks.append(PortfolioPosition(symbol=symbol, stock_name=stock_name, logo_url=logo_url, amount=next_amount, stock_value=None, stock_buyin_price=next_stock_buyin_price))
                    print(stocks)
                else:
                    print("Entering stocks:", stocks)
                    # update PortfolioPosition
                    prev_transaction = stocks[symbol_index]

                    """ Buy-In/Amount calculation """
                    prev_value = prev_transaction.amount * prev_transaction.stock_buyin_price # 5*120 = 600 + 5€ = 605€
                    next_value = next_amount * next_stock_buyin_price # 1*110€ + 10€ = 120€
                    print(prev_value, next_value)
                    if transaction_type == "buy":
                        prev_value += next_value-prev_value               # 605 + 290 = 895€
                        prev_transaction.amount += next_amount     # 5   + 3   = 8stk
                        capital -= (next_value + transaction_fee)
                    else:
                        prev_value -= next_value-prev_value
                        prev_transaction.amount -= next_amount
                        capital += (next_value - transaction_fee)

                    #new Buy-In price (division by zero)
                    if prev_transaction.amount <= 0:
                        stocks[symbol_index] = None
                        stocks.pop(symbol_index)
                    else:
                        prev_transaction.stock_buyin_price = prev_value/prev_transaction.amount # 895€ / 8stk
                        # override PortfolioPosition
                        stocks[symbol_index] = prev_transaction
                    print("Leaving stocks", stocks)



            # END IF date = transaction_date

        #END FOR - Transactions
        # stocks = remove_sold_stocks(stocks)

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

        current_depot_value = capital + current_depot_value
        ############################

        # portfolio_Value
        portfolio_value = PortfolioValue(current_depot_value, date)
        returned.append(portfolio_value)
        date += datetime.timedelta(days=1)
        # print("PortfolioValue for ", date, ": ", portfolio_value)
        # print("Cash for", date, ":", capital)

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
        current_date = transaction[0].stock_value.timestamp
        if min_date == None:
            min_date = current_date
        elif current_date < min_date:
            min_date = current_date

    return min_date
## End Support functions

def get_portfolio_analytics():
    pass

user = staticglobaldb.dbconn.get_user_by_auth_key("06eqq7LpJQOf9MS35yRcErFMxmMMUKdcRhEZ4dhXMQN2WHeVQnu1Dlvh6RZhNTeJvxM7moMCTghAE3i79KIV4Ynzzbql3m5KVxay2HDsKTgdok0UGz8qzwpk8NIxWREB")
transaction_list = staticglobaldb.dbconn.get_transactions_and_stock_by_user(user)
# print(__calculate_daily_change(user, transaction_list))
df = get_portfolio_history_pandas(user)
print(df)
# print(transaction_list)

# user = staticglobaldb.dbconn.get_user_by_auth_key("06eqq7LpJQOf9MS35yRcErFMxmMMUKdcRhEZ4dhXMQN2WHeVQnu1Dlvh6RZhNTeJvxM7moMCTghAE3i79KIV4Ynzzbql3m5KVxay2HDsKTgdok0UGz8qzwpk8NIxWREB")
# user.money_available = 10000000
# staticglobaldb.dbconn.update_user(user)
## TEST stock_values_available
# print(stock_values_available(user))

## TEST get_history
# history = get_portfolio_history(user)
# print(history)


# print(buy_stocks(user, "IBM", 1))
#
# print(user.first_name, user.last_name)
# history = get_portfolio_history(user)
# print(history)
# history = staticglobaldb.dbconn.get_stock_price_from_date()
# print(get_portfolio_positions(user))
# buy_stocks(user, "IBM", 1)
#
# history = get_portfolio_history(user)
# print(history)

# print("Buying 1 IBM stock for 100$")
# buy_stocks(user, 'IBM', 1)
# history = get_portfolio_history(user)
# print(history)
# print("Buying 1 IBM stock for 100$")
# sell_stocks(user, 'IBM', 1)
# history = get_portfolio_history(user)
# print(history)
# buy_stocks(user, "IBM", 1)

# history = get_portfolio_history(user)
# print(history)