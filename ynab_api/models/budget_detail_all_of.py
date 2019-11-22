# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ynab_api.configuration import Configuration


class BudgetDetailAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'accounts': 'list[Account]',
        'payees': 'list[Payee]',
        'payee_locations': 'list[PayeeLocation]',
        'category_groups': 'list[CategoryGroup]',
        'categories': 'list[Category]',
        'months': 'list[MonthDetail]',
        'transactions': 'list[TransactionSummary]',
        'subtransactions': 'list[SubTransaction]',
        'scheduled_transactions': 'list[ScheduledTransactionSummary]',
        'scheduled_subtransactions': 'list[ScheduledSubTransaction]'
    }

    attribute_map = {
        'accounts': 'accounts',
        'payees': 'payees',
        'payee_locations': 'payee_locations',
        'category_groups': 'category_groups',
        'categories': 'categories',
        'months': 'months',
        'transactions': 'transactions',
        'subtransactions': 'subtransactions',
        'scheduled_transactions': 'scheduled_transactions',
        'scheduled_subtransactions': 'scheduled_subtransactions'
    }

    def __init__(self, accounts=None, payees=None, payee_locations=None, category_groups=None, categories=None, months=None, transactions=None, subtransactions=None, scheduled_transactions=None, scheduled_subtransactions=None, local_vars_configuration=None):  # noqa: E501
        """BudgetDetailAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accounts = None
        self._payees = None
        self._payee_locations = None
        self._category_groups = None
        self._categories = None
        self._months = None
        self._transactions = None
        self._subtransactions = None
        self._scheduled_transactions = None
        self._scheduled_subtransactions = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if payees is not None:
            self.payees = payees
        if payee_locations is not None:
            self.payee_locations = payee_locations
        if category_groups is not None:
            self.category_groups = category_groups
        if categories is not None:
            self.categories = categories
        if months is not None:
            self.months = months
        if transactions is not None:
            self.transactions = transactions
        if subtransactions is not None:
            self.subtransactions = subtransactions
        if scheduled_transactions is not None:
            self.scheduled_transactions = scheduled_transactions
        if scheduled_subtransactions is not None:
            self.scheduled_subtransactions = scheduled_subtransactions

    @property
    def accounts(self):
        """Gets the accounts of this BudgetDetailAllOf.  # noqa: E501


        :return: The accounts of this BudgetDetailAllOf.  # noqa: E501
        :rtype: list[Account]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this BudgetDetailAllOf.


        :param accounts: The accounts of this BudgetDetailAllOf.  # noqa: E501
        :type: list[Account]
        """

        self._accounts = accounts

    @property
    def payees(self):
        """Gets the payees of this BudgetDetailAllOf.  # noqa: E501


        :return: The payees of this BudgetDetailAllOf.  # noqa: E501
        :rtype: list[Payee]
        """
        return self._payees

    @payees.setter
    def payees(self, payees):
        """Sets the payees of this BudgetDetailAllOf.


        :param payees: The payees of this BudgetDetailAllOf.  # noqa: E501
        :type: list[Payee]
        """

        self._payees = payees

    @property
    def payee_locations(self):
        """Gets the payee_locations of this BudgetDetailAllOf.  # noqa: E501


        :return: The payee_locations of this BudgetDetailAllOf.  # noqa: E501
        :rtype: list[PayeeLocation]
        """
        return self._payee_locations

    @payee_locations.setter
    def payee_locations(self, payee_locations):
        """Sets the payee_locations of this BudgetDetailAllOf.


        :param payee_locations: The payee_locations of this BudgetDetailAllOf.  # noqa: E501
        :type: list[PayeeLocation]
        """

        self._payee_locations = payee_locations

    @property
    def category_groups(self):
        """Gets the category_groups of this BudgetDetailAllOf.  # noqa: E501


        :return: The category_groups of this BudgetDetailAllOf.  # noqa: E501
        :rtype: list[CategoryGroup]
        """
        return self._category_groups

    @category_groups.setter
    def category_groups(self, category_groups):
        """Sets the category_groups of this BudgetDetailAllOf.


        :param category_groups: The category_groups of this BudgetDetailAllOf.  # noqa: E501
        :type: list[CategoryGroup]
        """

        self._category_groups = category_groups

    @property
    def categories(self):
        """Gets the categories of this BudgetDetailAllOf.  # noqa: E501


        :return: The categories of this BudgetDetailAllOf.  # noqa: E501
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this BudgetDetailAllOf.


        :param categories: The categories of this BudgetDetailAllOf.  # noqa: E501
        :type: list[Category]
        """

        self._categories = categories

    @property
    def months(self):
        """Gets the months of this BudgetDetailAllOf.  # noqa: E501


        :return: The months of this BudgetDetailAllOf.  # noqa: E501
        :rtype: list[MonthDetail]
        """
        return self._months

    @months.setter
    def months(self, months):
        """Sets the months of this BudgetDetailAllOf.


        :param months: The months of this BudgetDetailAllOf.  # noqa: E501
        :type: list[MonthDetail]
        """

        self._months = months

    @property
    def transactions(self):
        """Gets the transactions of this BudgetDetailAllOf.  # noqa: E501


        :return: The transactions of this BudgetDetailAllOf.  # noqa: E501
        :rtype: list[TransactionSummary]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this BudgetDetailAllOf.


        :param transactions: The transactions of this BudgetDetailAllOf.  # noqa: E501
        :type: list[TransactionSummary]
        """

        self._transactions = transactions

    @property
    def subtransactions(self):
        """Gets the subtransactions of this BudgetDetailAllOf.  # noqa: E501


        :return: The subtransactions of this BudgetDetailAllOf.  # noqa: E501
        :rtype: list[SubTransaction]
        """
        return self._subtransactions

    @subtransactions.setter
    def subtransactions(self, subtransactions):
        """Sets the subtransactions of this BudgetDetailAllOf.


        :param subtransactions: The subtransactions of this BudgetDetailAllOf.  # noqa: E501
        :type: list[SubTransaction]
        """

        self._subtransactions = subtransactions

    @property
    def scheduled_transactions(self):
        """Gets the scheduled_transactions of this BudgetDetailAllOf.  # noqa: E501


        :return: The scheduled_transactions of this BudgetDetailAllOf.  # noqa: E501
        :rtype: list[ScheduledTransactionSummary]
        """
        return self._scheduled_transactions

    @scheduled_transactions.setter
    def scheduled_transactions(self, scheduled_transactions):
        """Sets the scheduled_transactions of this BudgetDetailAllOf.


        :param scheduled_transactions: The scheduled_transactions of this BudgetDetailAllOf.  # noqa: E501
        :type: list[ScheduledTransactionSummary]
        """

        self._scheduled_transactions = scheduled_transactions

    @property
    def scheduled_subtransactions(self):
        """Gets the scheduled_subtransactions of this BudgetDetailAllOf.  # noqa: E501


        :return: The scheduled_subtransactions of this BudgetDetailAllOf.  # noqa: E501
        :rtype: list[ScheduledSubTransaction]
        """
        return self._scheduled_subtransactions

    @scheduled_subtransactions.setter
    def scheduled_subtransactions(self, scheduled_subtransactions):
        """Sets the scheduled_subtransactions of this BudgetDetailAllOf.


        :param scheduled_subtransactions: The scheduled_subtransactions of this BudgetDetailAllOf.  # noqa: E501
        :type: list[ScheduledSubTransaction]
        """

        self._scheduled_subtransactions = scheduled_subtransactions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BudgetDetailAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BudgetDetailAllOf):
            return True

        return self.to_dict() != other.to_dict()
