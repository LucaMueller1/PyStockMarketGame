import connexion

from swagger_server.models.api_error import ApiError  # noqa: E501
from swagger_server.models.portfolio_position import PortfolioPosition  # noqa: E501
from swagger_server.models.portfolio_value import PortfolioValue  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.transaction_prepare import TransactionPrepare  # noqa: E501
from swagger_server.models.user import User
from swagger_server.models.settings import Settings
from swagger_server import util
from swagger_server.controllers import staticglobaldb
from swagger_server.services.finance import finance_data
from swagger_server.services import trading_service
from swagger_server.models.user import User

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

        if transaction_prepare_param.amount <= 0:
            return ApiError(detail="Invalid stock quantity", status=400, title="Bad Request",
                            type="/portfolio/transaction"), 400

        user: User = staticglobaldb.dbconn.get_user_by_auth_key(api_key)  # will never return None because user is authorized
        settings: Settings = staticglobaldb.dbconn.get_settings_by_user(user)

        stock_quotation = finance_data.insert_stock_history_from_yfinance_to_db(transaction_prepare_param.symbol, "1d")
        transaction_value = (abs(transaction_prepare_param.amount) * stock_quotation.stock_price)

        print(transaction_prepare_param.transaction_type + "-Transaction from user: " + user.first_name + " of " + str(transaction_prepare_param.amount) + " " + transaction_prepare_param.symbol + ": " + str(transaction_value))

        if transaction_prepare_param.transaction_type.lower() == "buy":  # buy stock
            if user.money_available >= transaction_value:
                transaction = staticglobaldb.dbconn.insert_transaction(transaction_prepare_param, user)
                user.money_available = user.money_available - transaction_value - abs(settings.transaction_fee)  # absoulte value to make sure that user doesnt cheat
                staticglobaldb.dbconn.update_user(user)  # Update User in database
                return transaction
            else:
                return ApiError(detail="Insufficient cash", status=400, title="Bad Request",
                                type="/portfolio/transaction"), 400
        else:  # sell stock
            # check if buy-amount is sufficient
            available_positions = trading_service.stock_values_available(user)

            stock_available = False
            for item in available_positions:
                if item.symbol == transaction_prepare_param.symbol:
                    if item.amount >= transaction_prepare_param.amount:
                        stock_available = True
                    break

            if stock_available:
                transaction = staticglobaldb.dbconn.insert_transaction(transaction_prepare_param, user)
                user.money_available = (user.money_available + transaction_value) - abs(settings.transaction_fee)
                staticglobaldb.dbconn.update_user(user)  # Update User in database
                return transaction
            else:
                return ApiError(detail="Insufficient stock quantity to sell", status=400, title="Bad Request",
                                type="/portfolio/transaction"), 400

    return ApiError(detail="Failed to create transaction", status=400, title="Bad Request", type="/portfolio/transaction"), 400


def get_portfolio():  # noqa: E501
    """Get all current positions

    Returns all the current stock positions of the logged in user # noqa: E501


    :rtype: List[PortfolioPosition]
    """
    api_key = connexion.request.headers['api_key']
    user: User = staticglobaldb.dbconn.get_user_by_auth_key(api_key)

    portfolio_positions = trading_service.get_portfolio_positions(user)
    return portfolio_positions


def get_portfolio_value():  # noqa: E501
    """Get the performance of the portfolio

    Returns the logged in users portfolio performance # noqa: E501


    :rtype: List[PortfolioValue]
    """

    return 'do some magic!'
