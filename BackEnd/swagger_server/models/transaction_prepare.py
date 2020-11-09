# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TransactionPrepare(Model):
    """
    desc: TransactionPrepare represents an incoming stock buy/sell transaction of a user from the front-end. It only contains the symbol, amount and transaction type
    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, symbol: str=None, amount: int=None, transaction_type: str=None):  # noqa: E501
        """TransactionPrepare - a model defined in Swagger

        :param symbol: The symbol of this TransactionPrepare.  # noqa: E501
        :type symbol: str
        :param amount: The amount of this TransactionPrepare.  # noqa: E501
        :type amount: int
        :param transaction_type: The transaction_type of this TransactionPrepare.  # noqa: E501
        :type transaction_type: str
        """
        self.swagger_types = {
            'symbol': str,
            'amount': int,
            'transaction_type': str
        }

        self.attribute_map = {
            'symbol': 'symbol',
            'amount': 'amount',
            'transaction_type': 'transactionType'
        }

        self._symbol = symbol
        self._amount = amount
        self._transaction_type = transaction_type

    @classmethod
    def from_dict(cls, dikt) -> 'TransactionPrepare':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TransactionPrepare of this TransactionPrepare.  # noqa: E501
        :rtype: TransactionPrepare
        """
        return util.deserialize_model(dikt, cls)

    @property
    def symbol(self) -> str:
        """Gets the symbol of this TransactionPrepare.


        :return: The symbol of this TransactionPrepare.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str):
        """Sets the symbol of this TransactionPrepare.


        :param symbol: The symbol of this TransactionPrepare.
        :type symbol: str
        """

        self._symbol = symbol

    @property
    def amount(self) -> int:
        """Gets the amount of this TransactionPrepare.


        :return: The amount of this TransactionPrepare.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this TransactionPrepare.


        :param amount: The amount of this TransactionPrepare.
        :type amount: int
        """

        self._amount = amount

    @property
    def transaction_type(self) -> str:
        """Gets the transaction_type of this TransactionPrepare.


        :return: The transaction_type of this TransactionPrepare.
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type: str):
        """Sets the transaction_type of this TransactionPrepare.


        :param transaction_type: The transaction_type of this TransactionPrepare.
        :type transaction_type: str
        """
        allowed_values = ["buy", "sell"]  # noqa: E501
        if transaction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_type` ({0}), must be one of {1}"
                .format(transaction_type, allowed_values)
            )

        self._transaction_type = transaction_type
