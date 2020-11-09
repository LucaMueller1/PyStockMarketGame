# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.stock_value import StockValue
from swagger_server.models.base_model_ import Model
from swagger_server import util


class Transaction(Model):
    """
    desc: Transaction represents a stock buy/sell transaction of a user containing the bought stock as a ticker and its quotation
    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, id: int=None, stock_value: StockValue=None, amount: int=None, transaction_type: str=None, transaction_fee: float=None):  # noqa: E501
        """Transaction - a model defined in Swagger

        :param id: The id of this Transaction.  # noqa: E501
        :type id: int
        :param stock_value: The stock_value of this Transaction.  # noqa: E501
        :type stock_value: StockValue
        :param amount: The amount of this Transaction.  # noqa: E501
        :type amount: int
        :param transaction_type: The transaction_type of this Transaction.  # noqa: E501
        :type transaction_type: str
        :param transaction_fee: The transaction_fee of this Transaction.  # noqa: E501
        :type transaction_fee: float
        """
        self.swagger_types = {
            'id': int,
            'stock_value': StockValue,
            'amount': int,
            'transaction_type': str,
            'transaction_fee': float
        }

        self.attribute_map = {
            'id': 'id',
            'stock_value': 'stockValue',
            'amount': 'amount',
            'transaction_type': 'transactionType',
            'transaction_fee': 'transactionFee'
        }

        self._id = id
        self._stock_value = stock_value
        self._amount = amount
        self._transaction_type = transaction_type
        self._transaction_fee = transaction_fee

    @classmethod
    def from_dict(cls, dikt) -> 'Transaction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Transaction of this Transaction.  # noqa: E501
        :rtype: Transaction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Transaction.


        :return: The id of this Transaction.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Transaction.


        :param id: The id of this Transaction.
        :type id: int
        """

        self._id = id

    @property
    def stock_value(self) -> StockValue:
        """Gets the stock_value of this Transaction.


        :return: The stock_value of this Transaction.
        :rtype: StockValue
        """
        return self._stock_value

    @stock_value.setter
    def stock_value(self, stock_value: StockValue):
        """Sets the stock_value of this Transaction.


        :param stock_value: The stock_value of this Transaction.
        :type stock_value: StockValue
        """

        self._stock_value = stock_value

    @property
    def amount(self) -> int:
        """Gets the amount of this Transaction.


        :return: The amount of this Transaction.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this Transaction.


        :param amount: The amount of this Transaction.
        :type amount: int
        """

        self._amount = amount

    @property
    def transaction_type(self) -> str:
        """Gets the transaction_type of this Transaction.


        :return: The transaction_type of this Transaction.
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type: str):
        """Sets the transaction_type of this Transaction.


        :param transaction_type: The transaction_type of this Transaction.
        :type transaction_type: str
        """
        allowed_values = ["buy", "sell"]  # noqa: E501
        if transaction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_type` ({0}), must be one of {1}"
                .format(transaction_type, allowed_values)
            )

        self._transaction_type = transaction_type

    @property
    def transaction_fee(self) -> float:
        """Gets the transaction_fee of this Transaction.


        :return: The transaction_fee of this Transaction.
        :rtype: float
        """
        return self._transaction_fee

    @transaction_fee.setter
    def transaction_fee(self, transaction_fee: float):
        """Sets the transaction_fee of this Transaction.


        :param transaction_fee: The transaction_fee of this Transaction.
        :type transaction_fee: float
        """

        self._transaction_fee = transaction_fee
