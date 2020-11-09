# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StockSearchResult(Model):
    """
    desc: StockSearchResult is used to fill the search bar in the front-end with all available stocks in the database
    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, symbol: str=None, stock_name: str=None):  # noqa: E501
        """StockSearchResult - a model defined in Swagger

        :param symbol: The symbol of this StockSearchResult.  # noqa: E501
        :type symbol: str
        :param stock_name: The stock_name of this StockSearchResult.  # noqa: E501
        :type stock_name: str
        """
        self.swagger_types = {
            'symbol': str,
            'stock_name': str
        }

        self.attribute_map = {
            'symbol': 'symbol',
            'stock_name': 'stockName'
        }

        self._symbol = symbol
        self._stock_name = stock_name

    @classmethod
    def from_dict(cls, dikt) -> 'StockSearchResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StockSearchResult of this StockSearchResult.  # noqa: E501
        :rtype: StockSearchResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def symbol(self) -> str:
        """Gets the symbol of this StockSearchResult.


        :return: The symbol of this StockSearchResult.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str):
        """Sets the symbol of this StockSearchResult.


        :param symbol: The symbol of this StockSearchResult.
        :type symbol: str
        """

        self._symbol = symbol

    @property
    def stock_name(self) -> str:
        """Gets the stock_name of this StockSearchResult.


        :return: The stock_name of this StockSearchResult.
        :rtype: str
        """
        return self._stock_name

    @stock_name.setter
    def stock_name(self, stock_name: str):
        """Sets the stock_name of this StockSearchResult.


        :param stock_name: The stock_name of this StockSearchResult.
        :type stock_name: str
        """

        self._stock_name = stock_name
