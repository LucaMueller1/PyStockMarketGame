# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.portfolio_position import PortfolioPosition  # noqa: E501
from swagger_server.models.portfolio_value import PortfolioValue  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.transaction_prepare import TransactionPrepare  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPortfolioController(BaseTestCase):
    """PortfolioController integration test stubs"""

    def test_create_transaction(self):
        """Test case for create_transaction

        Create a new stock transaction
        """
        TransactionPrepare = TransactionPrepare()
        response = self.client.open(
            '/api/portfolio/transaction',
            method='POST',
            data=json.dumps(TransactionPrepare),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_portfolio(self):
        """Test case for get_portfolio

        Get all current positions
        """
        response = self.client.open(
            '/api/portfolio',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_portfolio_value(self):
        """Test case for get_portfolio_value

        Get the performance of the portfolio
        """
        response = self.client.open(
            '/api/portfolio/value',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
