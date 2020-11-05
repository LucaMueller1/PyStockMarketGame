import pandas as pd
from swagger_server.services.db_service import DatabaseConn
from swagger_server.models.portfolio_position import PortfolioPosition
from swagger_server.models.user import User
from swagger_server.services.finance import finance_data

def buy_stock(symbol: str, anzahl: int):
    # is there enough money
    # lock access to buying, selling (security)
    # buy stocks

    return True


def stock_values_available(symbol: str, anzahl: int):

    # get amount owned
    # check if anzahl >= amount owned
    pass
    return True


def get_portfolio_positions(user: User):
    """ !!! this does not calculate the history of the depot !!!
        This function creates a PortfolioPosition for every Stock that has been bought or sold
        in the past.
        it checks through every transaction made in the past and modifies it so that there is the average
        Buy-In price as well as the current amount of stocks owned.

    :param user: current user
    :return: Array of PortfolioPositions
    :test: make some transactions and go to the portfolio site of the stock.
    """
    # get all stock transactions
    conn = DatabaseConn()
    transactions = conn.get_transactions_and_stock_by_user(user)
    # print(transactions)

    # for every symbol
    stocks = []
    for transaction in transactions:
        symbol = transaction[1].symbol
        stock_name = transaction[1].stock_name
        next_amount = transaction[0].amount
        current_stock_price = 100
        transaction_fee = transaction[0].transaction_fee
        next_stock_buyin_price = transaction[0].stock_value.stock_price + (transaction_fee/next_amount) # price at buy
        transaction_type = transaction[0].transaction_type


        symbol_index = None
        found = False
        for i in range(len(stocks)):
            if stocks[i].symbol == symbol:
                found = True
                symbol_index = i
                break

        if not found:

            current_stock_price = finance_data.insert_stock_history_from_yfinance_to_db(symbol, "1d")
            stocks.append(PortfolioPosition(symbol, stock_name, next_amount, current_stock_price, next_stock_buyin_price))
        else:
            # get Portfoliopostition out of list
            prev_position = stocks[symbol_index] # 5 Aktien 120€ + 5€



            # Buy-In/Amount calculation
            prev_value = prev_position.amount * prev_position.stock_buyin_price # 5*120 = 600 + 5€ = 605€
            next_value = next_amount * next_stock_buyin_price # 3*95€ + 5€ = 290€

            if transaction_type == "buy":
                prev_value += next_value                # 605 + 290 = 895€
                prev_position.amount += next_amount     # 5   + 3   = 8stk
            else:
                prev_value -= next_value
                prev_position.amount -= next_amount

            #new Buy-In price (division by zero)
            if prev_position.amount <= 0:
                stocks[symbol_index] = None
                stocks.pop(symbol_index)
            else:
                prev_position.stock_buyin_price = prev_value/prev_position.amount # 895€ / 8stk

            # override PortfolioPosition
            stocks[symbol_index] = prev_position

            stocks[symbol_index]

    print(stocks)

    return stocks


def get_portfolio_history(user: User):
    """ Gives History of Portfolio for use in a graph

    :param user:
    :return:
    """
    pass


# user = User(2, "Luca", "Weissbeck", "lucaweissbeck@yahoo.de", '$2b$12$.7atD7IuL.LH0/XbGONOiu3l6aJ2Ux/1r2/ExWIsJYukcymy8181C', 10000, 10000)
# stock_portfolio_position(user)
# get_portfolio_positions(user)