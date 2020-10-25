import connexion
import six

from swagger_server.models.stock_financials import StockFinancials  # noqa: E501
from swagger_server.models.stock_info import StockInfo  # noqa: E501
from swagger_server.models.stock_value import StockValue  # noqa: E501
from swagger_server import util


def get_stock_financials(wkn):  # noqa: E501
    """Get financials of given stock

     # noqa: E501

    :param wkn: WKN of searched stock
    :type wkn: str

    :rtype: StockFinancials
    """
    return 'do some magic!'


def get_stock_history(wkn, period):  # noqa: E501
    """Get historical data of given stock

    Returns all available stocks from the database # noqa: E501

    :param wkn: WKN of searched stock
    :type wkn: str
    :param period: Period of stock data
    :type period: str

    :rtype: List[StockValue]
    """
    return 'do some magic!'


def get_stocks():  # noqa: E501
    """Get all stocks in database

    Returns all available stocks from the database # noqa: E501


    :rtype: List[StockInfo]
    """
    return 'do some magic!'
