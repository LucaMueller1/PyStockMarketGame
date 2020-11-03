import connexion
import six
import re

from swagger_server.models.api_error import ApiError  # noqa: E501
from swagger_server.models.stock_description import StockDescription  # noqa: E501
from swagger_server.models.stock_search_result import StockSearchResult  # noqa: E501
from swagger_server.models.stock_sustainability import StockSustainability  # noqa: E501
from swagger_server.models.stock_value import StockValue  # noqa: E501
from swagger_server import util
from swagger_server.controllers import staticglobaldb
from swagger_server.services.finance import finance_data


def get_stock_description(symbol):  # noqa: E501
    """Get financials of given stock

     # noqa: E501

    :param symbol: Symbol of searched stock
    :type symbol: str

    :rtype: StockDescription
    """
    description = finance_data.get_stock_info_from_yfinance(symbol)
    if description is None:
        return ApiError(detail="Description for given stock not found", status=404, title="Not Found",
                        type=("/stock/" + symbol + "/description"))

    return description


def get_stock_history(symbol, period):  # noqa: E501
    """Get historical data of given stock

    Returns all available stocks from the database # noqa: E501

    :param symbol: Symbol of searched stock
    :type symbol: str
    :param period: Period of stock data
    :type period: str

    :rtype: List[StockValue]
    :test 1mom returns ApiError, 7d returns list of stock_values
    """
    if not re.match("^\\d+(d$)|^\\d+(mo$)|^\\d+(y$)|^ytd$|^max$", period):
        return ApiError(detail="Given period not matching pattern", status=418, title="I'm a teapot",
                        type=("/stock/" + symbol + "/history"))
    finance_data.get_stock_history_from_yfinance(symbol, period)

    stock_value_list = list()

    if stock_value_list is None:
        return ApiError(detail="History for given stock not found", status=404, title="Not Found",
                    type=("/stock/" + symbol + "/history"))

    return stock_value_list


def get_stock_sustainability(symbol):  # noqa: E501
    """Get information about the sustainability of given stock

    Returns an object that describes the sustainability companies # noqa: E501

    :param symbol: Symbol of searched stock
    :type symbol: str

    :rtype: StockSustainability
    """
    return ApiError(detail="Sustainability-information for given stock not found", status=404, title="Not Found",
                    type=("/stock/" + symbol + "/sustainability"))


def get_stocks():  # noqa: E501
    """Get all stocks in database

    Returns all available stocks from the database # noqa: E501


    :rtype: List[StockSearchResult]
    """

    stock_list = staticglobaldb.dbconn.get_stock_search_results()

    if (stock_list is None) or (len(stock_list) < 1):
        return 'No Content', 204
    return stock_list
