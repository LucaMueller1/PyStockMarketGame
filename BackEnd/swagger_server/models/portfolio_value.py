# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PortfolioValue(Model):
    """
    desc: PortfolioValue represents the value of the entire portfolio of a user at a certain date
    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, market_value: float=None, timestamp: datetime=None):  # noqa: E501
        """PortfolioValue - a model defined in Swagger

        :param market_value: The market_value of this PortfolioValue.  # noqa: E501
        :type market_value: float
        :param timestamp: The timestamp of this PortfolioValue.  # noqa: E501
        :type timestamp: datetime
        """
        self.swagger_types = {
            'market_value': float,
            'timestamp': datetime
        }

        self.attribute_map = {
            'market_value': 'marketValue',
            'timestamp': 'timestamp'
        }

        self._market_value = market_value
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'PortfolioValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PortfolioValue of this PortfolioValue.  # noqa: E501
        :rtype: PortfolioValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def market_value(self) -> float:
        """Gets the market_value of this PortfolioValue.


        :return: The market_value of this PortfolioValue.
        :rtype: float
        """
        return self._market_value

    @market_value.setter
    def market_value(self, market_value: float):
        """Sets the market_value of this PortfolioValue.


        :param market_value: The market_value of this PortfolioValue.
        :type market_value: float
        """

        self._market_value = market_value

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this PortfolioValue.


        :return: The timestamp of this PortfolioValue.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this PortfolioValue.


        :param timestamp: The timestamp of this PortfolioValue.
        :type timestamp: datetime
        """

        self._timestamp = timestamp
