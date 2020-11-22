"""
desc: Portfolio Controller that handles requests for buying/selling stock and returning portfolio data
author: Luca Mueller
date: 2020-10-14
"""

import connexion

from swagger_server.controllers import staticglobaldb
from swagger_server.models.api_error import ApiError  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.transaction_prepare import TransactionPrepare  # noqa: E501
from swagger_server.models.user import User
from swagger_server.services import trading_service


def create_transaction(transaction_prepare_param):  # noqa: E501
    """Create a new stock transaction

    Creates and executes a transaction for the logged in user # noqa: E501

    :param transaction_prepare_param: The transaction to create.
    :type transaction_prepare_param: dict | bytes

    :rtype: Transaction
    :test Correct: Request with valid transaction_prepare_param object in body (according to swagger doc) (here: {"symbol": "AAPL","amount": 10,"transactionType": "buy"},  returns executed transaction object. Incorrect: Request with invalid object in body (e.g. symbol LOL) returns internal Error object
    """
    if connexion.request.is_json:
        transaction_prepare_param = TransactionPrepare.from_dict(connexion.request.get_json())  # noqa: E501
        api_key = connexion.request.headers['api_key']

        if transaction_prepare_param.amount <= 0:
            return ApiError(detail="Invalid stock quantity", status=400, title="Bad Request",
                            type="/portfolio/transaction"), 400

        user: User = staticglobaldb.dbconn.get_user_by_auth_key(api_key)  # will never return None because user must be authorized to call this request

        print(transaction_prepare_param.transaction_type + "-Transaction from user: " + user.first_name + " of " + str(transaction_prepare_param.amount) + " " + transaction_prepare_param.symbol)

        if transaction_prepare_param.transaction_type.lower() == "buy":  # buy stock
            transaction = trading_service.buy_stocks(user, transaction_prepare_param.symbol, transaction_prepare_param.amount)
            if transaction is not None:
                return transaction
            else:
                return ApiError(detail="Insufficient cash", status=400, title="Bad Request",
                                type="/portfolio/transaction"), 400
        else:  # sell stock
            transaction = trading_service.sell_stocks(user, transaction_prepare_param.symbol, transaction_prepare_param.amount)
            if transaction is not None:
                return transaction
            else:
                return ApiError(detail="Insufficient stock quantity to sell", status=400, title="Bad Request",
                                type="/portfolio/transaction"), 400

    return ApiError(detail="Failed to create transaction", status=400, title="Bad Request", type="/portfolio/transaction"), 400


def get_portfolio():  # noqa: E501
    """Get all current positions

    Returns all the current stock positions of the logged in user # noqa: E501


    :rtype: List[PortfolioPosition]
    :test Correct: Request with valid api_key returns list of all portfolio positions for that user. Incorrect: Request with invalid api_key returns unauthorized error object
    """
    api_key = connexion.request.headers['api_key']
    user: User = staticglobaldb.dbconn.get_user_by_auth_key(api_key)

    portfolio_positions = trading_service.get_portfolio_positions(user)
    return portfolio_positions


def get_portfolio_value():  # noqa: E501
    """Get the performance of the portfolio

    Returns the logged in users portfolio performance # noqa: E501


    :rtype: List[PortfolioValue]
    :test Correct: Request with valid api_key returns list of portfolioValue objects that can be used to draw a graph. Incorrect: Request with invalid api_key returns unauthorized error object
    """
    api_key = connexion.request.headers['api_key']
    user: User = staticglobaldb.dbconn.get_user_by_auth_key(api_key)

    portfolio_value = trading_service.get_portfolio_history_pandas(user)
    return portfolio_value
