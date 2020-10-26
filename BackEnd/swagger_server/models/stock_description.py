# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StockDescription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, symbol: str=None, stock_name: str=None, country_id: str=None, logo_url: str=None, long_description: str=None, industry: str=None, dividend: str=None, info_loaded: bool=None, history_loaded: bool=None):  # noqa: E501
        """StockDescription - a model defined in Swagger

        :param symbol: The symbol of this StockDescription.  # noqa: E501
        :type symbol: str
        :param stock_name: The stock_name of this StockDescription.  # noqa: E501
        :type stock_name: str
        :param country_id: The country_id of this StockDescription.  # noqa: E501
        :type country_id: str
        :param logo_url: The logo_url of this StockDescription.  # noqa: E501
        :type logo_url: str
        :param long_description: The long_description of this StockDescription.  # noqa: E501
        :type long_description: str
        :param industry: The industry of this StockDescription.  # noqa: E501
        :type industry: str
        :param dividend: The dividend of this StockDescription.  # noqa: E501
        :type dividend: str
        :param info_loaded: The info_loaded of this StockDescription.  # noqa: E501
        :type info_loaded: bool
        :param history_loaded: The history_loaded of this StockDescription.  # noqa: E501
        :type history_loaded: bool
        """
        self.swagger_types = {
            'symbol': str,
            'stock_name': str,
            'country_id': str,
            'logo_url': str,
            'long_description': str,
            'industry': str,
            'dividend': str,
            'info_loaded': bool,
            'history_loaded': bool
        }

        self.attribute_map = {
            'symbol': 'symbol',
            'stock_name': 'stockName',
            'country_id': 'countryId',
            'logo_url': 'logoUrl',
            'long_description': 'longDescription',
            'industry': 'industry',
            'dividend': 'dividend',
            'info_loaded': 'infoLoaded',
            'history_loaded': 'historyLoaded'
        }

        self._symbol = symbol
        self._stock_name = stock_name
        self._country_id = country_id
        self._logo_url = logo_url
        self._long_description = long_description
        self._industry = industry
        self._dividend = dividend
        self._info_loaded = info_loaded
        self._history_loaded = history_loaded

    @classmethod
    def from_dict(cls, dikt) -> 'StockDescription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StockDescription of this StockDescription.  # noqa: E501
        :rtype: StockDescription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def symbol(self) -> str:
        """Gets the symbol of this StockDescription.


        :return: The symbol of this StockDescription.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str):
        """Sets the symbol of this StockDescription.


        :param symbol: The symbol of this StockDescription.
        :type symbol: str
        """

        self._symbol = symbol

    @property
    def stock_name(self) -> str:
        """Gets the stock_name of this StockDescription.


        :return: The stock_name of this StockDescription.
        :rtype: str
        """
        return self._stock_name

    @stock_name.setter
    def stock_name(self, stock_name: str):
        """Sets the stock_name of this StockDescription.


        :param stock_name: The stock_name of this StockDescription.
        :type stock_name: str
        """

        self._stock_name = stock_name

    @property
    def country_id(self) -> str:
        """Gets the country_id of this StockDescription.


        :return: The country_id of this StockDescription.
        :rtype: str
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id: str):
        """Sets the country_id of this StockDescription.


        :param country_id: The country_id of this StockDescription.
        :type country_id: str
        """

        self._country_id = country_id

    @property
    def logo_url(self) -> str:
        """Gets the logo_url of this StockDescription.


        :return: The logo_url of this StockDescription.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url: str):
        """Sets the logo_url of this StockDescription.


        :param logo_url: The logo_url of this StockDescription.
        :type logo_url: str
        """

        self._logo_url = logo_url

    @property
    def long_description(self) -> str:
        """Gets the long_description of this StockDescription.


        :return: The long_description of this StockDescription.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description: str):
        """Sets the long_description of this StockDescription.


        :param long_description: The long_description of this StockDescription.
        :type long_description: str
        """

        self._long_description = long_description

    @property
    def industry(self) -> str:
        """Gets the industry of this StockDescription.


        :return: The industry of this StockDescription.
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry: str):
        """Sets the industry of this StockDescription.


        :param industry: The industry of this StockDescription.
        :type industry: str
        """

        self._industry = industry

    @property
    def dividend(self) -> str:
        """Gets the dividend of this StockDescription.


        :return: The dividend of this StockDescription.
        :rtype: str
        """
        return self._dividend

    @dividend.setter
    def dividend(self, dividend: str):
        """Sets the dividend of this StockDescription.


        :param dividend: The dividend of this StockDescription.
        :type dividend: str
        """

        self._dividend = dividend

    @property
    def info_loaded(self) -> bool:
        """Gets the info_loaded of this StockDescription.


        :return: The info_loaded of this StockDescription.
        :rtype: bool
        """
        return self._info_loaded

    @info_loaded.setter
    def info_loaded(self, info_loaded: bool):
        """Sets the info_loaded of this StockDescription.


        :param info_loaded: The info_loaded of this StockDescription.
        :type info_loaded: bool
        """

        self._info_loaded = info_loaded

    @property
    def history_loaded(self) -> bool:
        """Gets the history_loaded of this StockDescription.


        :return: The history_loaded of this StockDescription.
        :rtype: bool
        """
        return self._history_loaded

    @history_loaded.setter
    def history_loaded(self, history_loaded: bool):
        """Sets the history_loaded of this StockDescription.


        :param history_loaded: The history_loaded of this StockDescription.
        :type history_loaded: bool
        """

        self._history_loaded = history_loaded