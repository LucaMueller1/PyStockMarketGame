# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StockSustainability(Model):
    """
    desc: StockSustainability contains a symbol and should contain a number of describing attributes like
    animal_testing=false etc. This class can be solely described by a dict with key-value pairs

    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, symbol: str=None):  # noqa: E501
        """StockSustainability - a model defined in Swagger

        :param symbol: The symbol of this StockSustainability.  # noqa: E501
        :type symbol: str
        """
        self.swagger_types = {
            'symbol': str
        }

        self.attribute_map = {
            'symbol': 'symbol'
        }

        self._symbol = symbol

    @classmethod
    def from_dict(cls, dikt) -> 'StockSustainability':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StockSustainability of this StockSustainability.  # noqa: E501
        :rtype: StockSustainability
        """
        return util.deserialize_model(dikt, cls)

    @property
    def symbol(self) -> str:
        """Gets the symbol of this StockSustainability.


        :return: The symbol of this StockSustainability.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str):
        """Sets the symbol of this StockSustainability.


        :param symbol: The symbol of this StockSustainability.
        :type symbol: str
        """

        self._symbol = symbol
