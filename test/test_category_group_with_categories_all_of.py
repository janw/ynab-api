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
from ynab_api.models.category_group_with_categories_all_of import CategoryGroupWithCategoriesAllOf  # noqa: E501
from ynab_api.rest import ApiException

class TestCategoryGroupWithCategoriesAllOf(unittest.TestCase):
    """CategoryGroupWithCategoriesAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CategoryGroupWithCategoriesAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ynab_api.models.category_group_with_categories_all_of.CategoryGroupWithCategoriesAllOf()  # noqa: E501
        if include_optional :
            return CategoryGroupWithCategoriesAllOf(
                categories = [
                    ynab_api.models.category.Category(
                        id = '0', 
                        category_group_id = '0', 
                        name = '0', 
                        hidden = True, 
                        original_category_group_id = '0', 
                        note = '0', 
                        budgeted = 56, 
                        activity = 56, 
                        balance = 56, 
                        goal_type = 'TB', 
                        goal_creation_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        goal_target = 56, 
                        goal_target_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        goal_percentage_complete = 56, 
                        deleted = True, )
                    ]
            )
        else :
            return CategoryGroupWithCategoriesAllOf(
                categories = [
                    ynab_api.models.category.Category(
                        id = '0', 
                        category_group_id = '0', 
                        name = '0', 
                        hidden = True, 
                        original_category_group_id = '0', 
                        note = '0', 
                        budgeted = 56, 
                        activity = 56, 
                        balance = 56, 
                        goal_type = 'TB', 
                        goal_creation_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        goal_target = 56, 
                        goal_target_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        goal_percentage_complete = 56, 
                        deleted = True, )
                    ],
        )

    def testCategoryGroupWithCategoriesAllOf(self):
        """Test CategoryGroupWithCategoriesAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
