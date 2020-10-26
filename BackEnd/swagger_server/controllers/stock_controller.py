import connexion
import six

from swagger_server.models.stock_description import StockDescription  # noqa: E501
from swagger_server.models.stock_search_result import StockSearchResult  # noqa: E501
from swagger_server.models.stock_value import StockValue  # noqa: E501
from swagger_server import util


def get_stock_description(symbol):  # noqa: E501
    """Get financials of given stock

     # noqa: E501

    :param symbol: Symbol of searched stock
    :type symbol: str

    :rtype: StockDescription
    """
    return 'do some magic!'


def get_stock_history(symbol, period):  # noqa: E501
    """Get historical data of given stock

    Returns all available stocks from the database # noqa: E501

    :param symbol: Symbol of searched stock
    :type symbol: str
    :param period: Period of stock data
    :type period: str

    :rtype: List[StockValue]
    """
    return 'do some magic!'


def get_stocks():  # noqa: E501
    """Get all stocks in database

    Returns all available stocks from the database # noqa: E501


    :rtype: List[StockSearchResult]
    """
    return 'do some magic!'