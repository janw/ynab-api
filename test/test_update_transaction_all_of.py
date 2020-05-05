# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ynab_api
from ynab_api.models.update_transaction_all_of import UpdateTransactionAllOf  # noqa: E501
from ynab_api.rest import ApiException

class TestUpdateTransactionAllOf(unittest.TestCase):
    """UpdateTransactionAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateTransactionAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ynab_api.models.update_transaction_all_of.UpdateTransactionAllOf()  # noqa: E501
        if include_optional :
            return UpdateTransactionAllOf(
                id = '0'
            )
        else :
            return UpdateTransactionAllOf(
                id = '0',
        )

    def testUpdateTransactionAllOf(self):
        """Test UpdateTransactionAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
