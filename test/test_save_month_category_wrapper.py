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
from ynab_api.models.save_month_category_wrapper import SaveMonthCategoryWrapper  # noqa: E501
from ynab_api.rest import ApiException

class TestSaveMonthCategoryWrapper(unittest.TestCase):
    """SaveMonthCategoryWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SaveMonthCategoryWrapper
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ynab_api.models.save_month_category_wrapper.SaveMonthCategoryWrapper()  # noqa: E501
        if include_optional :
            return SaveMonthCategoryWrapper(
                category = ynab_api.models.save_month_category.SaveMonthCategory(
                    budgeted = 56, )
            )
        else :
            return SaveMonthCategoryWrapper(
                category = ynab_api.models.save_month_category.SaveMonthCategory(
                    budgeted = 56, ),
        )

    def testSaveMonthCategoryWrapper(self):
        """Test SaveMonthCategoryWrapper"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
