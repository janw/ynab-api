# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ynab_api
from ynab_api.api.transactions_api import TransactionsApi  # noqa: E501
from ynab_api.rest import ApiException


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self):
        self.api = ynab_api.api.transactions_api.TransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_transaction(self):
        """Test case for create_transaction

        Create a single transaction or multiple transactions  # noqa: E501
        """
        pass

    def test_get_transaction_by_id(self):
        """Test case for get_transaction_by_id

        Single transaction  # noqa: E501
        """
        pass

    def test_get_transactions(self):
        """Test case for get_transactions

        List transactions  # noqa: E501
        """
        pass

    def test_get_transactions_by_account(self):
        """Test case for get_transactions_by_account

        List account transactions  # noqa: E501
        """
        pass

    def test_get_transactions_by_category(self):
        """Test case for get_transactions_by_category

        List category transactions  # noqa: E501
        """
        pass

    def test_get_transactions_by_payee(self):
        """Test case for get_transactions_by_payee

        List payee transactions  # noqa: E501
        """
        pass

    def test_update_transaction(self):
        """Test case for update_transaction

        Updates an existing transaction  # noqa: E501
        """
        pass

    def test_update_transactions(self):
        """Test case for update_transactions

        Update multiple transactions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
