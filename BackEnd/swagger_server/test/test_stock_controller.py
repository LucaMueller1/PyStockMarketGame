# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.stock_financials import StockFinancials  # noqa: E501
from swagger_server.models.stock_info import StockInfo  # noqa: E501
from swagger_server.models.stock_value import StockValue  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStockController(BaseTestCase):
    """StockController integration test stubs"""

    def test_get_stock_financials(self):
        """Test case for get_stock_financials

        Get financials of given stock
        """
        response = self.client.open(
            '/api/stock/{wkn}/financials'.format(wkn='wkn_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_stock_history(self):
        """Test case for get_stock_history

        Get historical data of given stock
        """
        query_string = [('period', 'period_example')]
        response = self.client.open(
            '/api/stock/{wkn}/history'.format(wkn='wkn_example'),
            method='GET',
            query_string=query_string)
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
