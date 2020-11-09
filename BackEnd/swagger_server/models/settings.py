# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Settings(Model):
    """
    desc: Settings represent the settings object for a user containing the transaction-fee
    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, transaction_fee: float=None):  # noqa: E501
        """Settings - a model defined in Swagger

        :param transaction_fee: The transaction_fee of this Settings.  # noqa: E501
        :type transaction_fee: float
        """
        self.swagger_types = {
            'transaction_fee': float
        }

        self.attribute_map = {
            'transaction_fee': 'transactionFee'
        }

        self._transaction_fee = transaction_fee

    @classmethod
    def from_dict(cls, dikt) -> 'Settings':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Settings of this Settings.  # noqa: E501
        :rtype: Settings
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transaction_fee(self) -> float:
        """Gets the transaction_fee of this Settings.


        :return: The transaction_fee of this Settings.
        :rtype: float
        """
        return self._transaction_fee

    @transaction_fee.setter
    def transaction_fee(self, transaction_fee: float):
        """Sets the transaction_fee of this Settings.


        :param transaction_fee: The transaction_fee of this Settings.
        :type transaction_fee: float
        """

        self._transaction_fee = transaction_fee
