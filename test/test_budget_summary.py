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
from ynab_api.models.budget_summary import BudgetSummary  # noqa: E501
from ynab_api.rest import ApiException

class TestBudgetSummary(unittest.TestCase):
    """BudgetSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BudgetSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ynab_api.models.budget_summary.BudgetSummary()  # noqa: E501
        if include_optional :
            return BudgetSummary(
                id = '0', 
                name = '0', 
                last_modified_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                first_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                last_month = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                date_format = ynab_api.models.date_format.DateFormat(
                    format = '0', ), 
                currency_format = ynab_api.models.currency_format.CurrencyFormat(
                    iso_code = '0', 
                    example_format = '0', 
                    decimal_digits = 56, 
                    decimal_separator = '0', 
                    symbol_first = True, 
                    group_separator = '0', 
                    currency_symbol = '0', 
                    display_symbol = True, ), 
                accounts = [
                    ynab_api.models.account.Account(
                        id = '0', 
                        name = '0', 
                        type = 'checking', 
                        on_budget = True, 
                        closed = True, 
                        note = '0', 
                        balance = 56, 
                        cleared_balance = 56, 
                        uncleared_balance = 56, 
                        transfer_payee_id = '0', 
                        deleted = True, )
                    ]
            )
        else :
            return BudgetSummary(
                id = '0',
                name = '0',
        )

    def testBudgetSummary(self):
        """Test BudgetSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
