# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_error import ApiError  # noqa: E501
from swagger_server.models.stock_description import StockDescription  # noqa: E501
from swagger_server.models.stock_search_result import StockSearchResult  # noqa: E501
from swagger_server.models.stock_sustainability import StockSustainability  # noqa: E501
from swagger_server.models.stock_value import StockValue  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStockController(BaseTestCase):
    """StockController integration test stubs"""

    def test_get_stock_description(self):
        """Test case for get_stock_description

        Get financials of given stock
        """
        response = self.client.open(
            '/api/stock/{symbol}/description'.format(symbol='symbol_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_stock_history(self):
        """Test case for get_stock_history

        Get historical data of given stock
        """
        query_string = [('period', 'period_example')]
        response = self.client.open(
            '/api/stock/{symbol}/history'.format(symbol='symbol_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_stock_sustainability(self):
        """Test case for get_stock_sustainability

        Get information about the sustainability of given stock
        """
        response = self.client.open(
            '/api/stock/{symbol}/sustainability'.format(symbol='symbol_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_stocks(self):
        """Test case for get_stocks

        Get all stocks in database
        """
        response = self.client.open(
            '/api/stock',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
