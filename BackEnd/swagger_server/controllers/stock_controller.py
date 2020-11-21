"""
desc: Stock Controller that handles all requests containing stock information
author: Luca Mueller
date: 2020-11-07
"""

import re

from swagger_server.controllers import staticglobaldb
from swagger_server.models.api_error import ApiError  # noqa: E501
from swagger_server.models.stock_description import StockDescription  # noqa: E501
from swagger_server.models.stock_sustainability import StockSustainability  # noqa: E501
from swagger_server.services.finance import finance_data


def get_stock_description(symbol):  # noqa: E501
    """Get financials of given stock

    Returns financials which include dividend, p/e-value and much more # noqa: E501

    :param symbol: Symbol of searched stock
    :type symbol: str

    :rtype: StockDescription
    :test Correct: Request with symbol AAPL returns full description object. Incorrect: Request with symbol LOL returns internal Error object
    """
    description = finance_data.get_stock_info_from_yfinance(symbol)
    if description is None:
        return ApiError(detail="Description for given stock not found", status=404, title="Not Found",
                        type=("/stock/" + symbol + "/description")), 404

    return description


def get_stock_history(symbol, period):  # noqa: E501
    """Get historical data of given stock

    Returns all available stocks from the database # noqa: E501

    :param symbol: Symbol of searched stock
    :type symbol: str
    :param period: Period of stock data
    :type period: str

    :rtype: List[StockValue]
    :test Correct: 7d returns list of stock_values in period of 7 days. Incorrect: 1mom returns ApiError
    """
    if not re.match("^\\d+(d$)|^\\d+(mo$)|^\\d+(y$)|^ytd$|^max$", period):
        return ApiError(detail="Given period not matching pattern", status=404, title="Not Found",
                        type=("/stock/" + symbol + "/history")), 404

    stock_value_list = finance_data.get_stock_history_to_frontend(symbol, period)

    if stock_value_list is None:
        return ApiError(detail="History for given stock not found", status=404, title="Not Found",
                        type=("/stock/" + symbol + "/history")), 404

    return stock_value_list


def get_stock_sustainability(symbol):  # noqa: E501
    """Get information about the sustainability of given stock

    Returns sustainability object that contains vital environmental data of the given stock  # noqa: E501

    :param symbol: Symbol of searched stock
    :type symbol: str

    :rtype: StockSustainability
    :test Correct: Request with symbol AAPL returns full sustainability object. Incorrect: Request with symbol LOL returns internal Error object
    """
    sustainability = finance_data.get_stock_sustainability(symbol)
    return sustainability

    # return ApiError(detail="Sustainability-information for given stock not found", status=404, title="Not Found",
    #                 type=("/stock/" + symbol + "/sustainability")), 404


def get_stocks():  # noqa: E501
    """Get all stocks in database

    Returns all available stocks from the database # noqa: E501


    :rtype: List[StockSearchResult]
    :test Correct: Request with valid api_key returns list of all stocks in database. Incorrect: Request with invalid api_key returns unauthorized error object
    """
    stock_list = staticglobaldb.dbconn.get_stock_search_results()
    return stock_list
