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
from ynab_api.api.categories_api import CategoriesApi  # noqa: E501
from ynab_api.rest import ApiException


class TestCategoriesApi(unittest.TestCase):
    """CategoriesApi unit test stubs"""

    def setUp(self):
        self.api = ynab_api.api.categories_api.CategoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_categories(self):
        """Test case for get_categories

        List categories  # noqa: E501
        """
        pass

    def test_get_category_by_id(self):
        """Test case for get_category_by_id

        Single category  # noqa: E501
        """
        pass

    def test_get_month_category_by_id(self):
        """Test case for get_month_category_by_id

        Single category for a specific budget month  # noqa: E501
        """
        pass

    def test_update_month_category(self):
        """Test case for update_month_category

        Update a category for a specific month  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
