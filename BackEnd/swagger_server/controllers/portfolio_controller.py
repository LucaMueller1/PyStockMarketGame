import connexion
import six

from swagger_server.models.api_error import ApiError  # noqa: E501
from swagger_server.models.portfolio_position import PortfolioPosition  # noqa: E501
from swagger_server.models.portfolio_value import PortfolioValue  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.transaction_prepare import TransactionPrepare  # noqa: E501
from swagger_server import util
from swagger_server.controllers import staticglobaldb
from swagger_server.services.finance import finance_data

"""
desc: Portfolio Controller that handles requests for buying/selling stock and returning portfolio data

author: Luca Mueller

date: 2020-10-14

mail: lucamueller32@gmail.com

version: 1.0

license: NONE
"""


def create_transaction(transaction_prepare_param):  # noqa: E501
    """Create a new stock transaction

    Creates and executes a transaction for the logged in user # noqa: E501

    :param transaction_prepare_param: The transaction to create.
    :type transaction_prepare_param: dict | bytes

    :rtype: Transaction
    """
    if connexion.request.is_json:
        transaction_prepare_param = TransactionPrepare.from_dict(connexion.request.get_json())  # noqa: E501
        api_key = connexion.request.headers['api_key']
        user = staticglobaldb.dbconn.get_user_by_auth_key(api_key)  # will never return None because user is authorized
        stock_quotation = finance_data.insert_stock_history_from_yfinance_to_db(transaction_prepare_param.symbol, "1d")
        transaction_value = (transaction_prepare_param.amount * stock_quotation.stock_price)

        if transaction_prepare_param.transaction_type.lower() == "buy":  # buy stock
            if user.money_available >= transaction_value:
                transaction = staticglobaldb.dbconn.insert_transaction(transaction_prepare_param, user)
                user.money_available(user.money_available - transaction_value)
                return transaction
            else:
                return ApiError(detail="Insufficient cash", status=400, title="Bad Request",
                                type="/portfolio/transaction")
        else:  # sell stock
            # check if buy-amount is sufficient
            transaction = staticglobaldb.dbconn.insert_transaction(transaction_prepare_param, user)
            user.money_available(user.money_available + transaction_value)
            return transaction

    return ApiError(detail="Failed to create transaction", status=400, title="Bad Request", type="/portfolio/transaction")


def get_portfolio():  # noqa: E501
    """Get all current positions

    Returns all the current stock positions of the logged in user # noqa: E501


    :rtype: List[PortfolioPosition]
    """
    return 'do some magic!'


def get_portfolio_value():  # noqa: E501
    """Get the performance of the portfolio

    Returns the logged in users portfolio performance # noqa: E501


    :rtype: List[PortfolioValue]
    """
    return 'do some magic!'
