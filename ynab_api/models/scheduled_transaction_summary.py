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


class ScheduledTransactionSummary(object):
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
        'id': 'str',
        'date_first': 'date',
        'date_next': 'date',
        'frequency': 'str',
        'amount': 'int',
        'memo': 'str',
        'flag_color': 'str',
        'account_id': 'str',
        'payee_id': 'str',
        'category_id': 'str',
        'transfer_account_id': 'str',
        'deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'date_first': 'date_first',
        'date_next': 'date_next',
        'frequency': 'frequency',
        'amount': 'amount',
        'memo': 'memo',
        'flag_color': 'flag_color',
        'account_id': 'account_id',
        'payee_id': 'payee_id',
        'category_id': 'category_id',
        'transfer_account_id': 'transfer_account_id',
        'deleted': 'deleted'
    }

    def __init__(self, id=None, date_first=None, date_next=None, frequency=None, amount=None, memo=None, flag_color=None, account_id=None, payee_id=None, category_id=None, transfer_account_id=None, deleted=None, local_vars_configuration=None):  # noqa: E501
        """ScheduledTransactionSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._date_first = None
        self._date_next = None
        self._frequency = None
        self._amount = None
        self._memo = None
        self._flag_color = None
        self._account_id = None
        self._payee_id = None
        self._category_id = None
        self._transfer_account_id = None
        self._deleted = None
        self.discriminator = None

        self.id = id
        self.date_first = date_first
        self.date_next = date_next
        self.frequency = frequency
        self.amount = amount
        if memo is not None:
            self.memo = memo
        if flag_color is not None:
            self.flag_color = flag_color
        self.account_id = account_id
        if payee_id is not None:
            self.payee_id = payee_id
        if category_id is not None:
            self.category_id = category_id
        if transfer_account_id is not None:
            self.transfer_account_id = transfer_account_id
        self.deleted = deleted

    @property
    def id(self):
        """Gets the id of this ScheduledTransactionSummary.  # noqa: E501


        :return: The id of this ScheduledTransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScheduledTransactionSummary.


        :param id: The id of this ScheduledTransactionSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def date_first(self):
        """Gets the date_first of this ScheduledTransactionSummary.  # noqa: E501

        The first date for which the Scheduled Transaction was scheduled.  # noqa: E501

        :return: The date_first of this ScheduledTransactionSummary.  # noqa: E501
        :rtype: date
        """
        return self._date_first

    @date_first.setter
    def date_first(self, date_first):
        """Sets the date_first of this ScheduledTransactionSummary.

        The first date for which the Scheduled Transaction was scheduled.  # noqa: E501

        :param date_first: The date_first of this ScheduledTransactionSummary.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and date_first is None:  # noqa: E501
            raise ValueError("Invalid value for `date_first`, must not be `None`")  # noqa: E501

        self._date_first = date_first

    @property
    def date_next(self):
        """Gets the date_next of this ScheduledTransactionSummary.  # noqa: E501

        The next date for which the Scheduled Transaction is scheduled.  # noqa: E501

        :return: The date_next of this ScheduledTransactionSummary.  # noqa: E501
        :rtype: date
        """
        return self._date_next

    @date_next.setter
    def date_next(self, date_next):
        """Sets the date_next of this ScheduledTransactionSummary.

        The next date for which the Scheduled Transaction is scheduled.  # noqa: E501

        :param date_next: The date_next of this ScheduledTransactionSummary.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and date_next is None:  # noqa: E501
            raise ValueError("Invalid value for `date_next`, must not be `None`")  # noqa: E501

        self._date_next = date_next

    @property
    def frequency(self):
        """Gets the frequency of this ScheduledTransactionSummary.  # noqa: E501


        :return: The frequency of this ScheduledTransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this ScheduledTransactionSummary.


        :param frequency: The frequency of this ScheduledTransactionSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and frequency is None:  # noqa: E501
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501
        allowed_values = ["never", "daily", "weekly", "everyOtherWeek", "twiceAMonth", "every4Weeks", "monthly", "everyOtherMonth", "every3Months", "every4Months", "twiceAYear", "yearly", "everyOtherYear"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and frequency not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

    @property
    def amount(self):
        """Gets the amount of this ScheduledTransactionSummary.  # noqa: E501

        The scheduled transaction amount in milliunits format  # noqa: E501

        :return: The amount of this ScheduledTransactionSummary.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ScheduledTransactionSummary.

        The scheduled transaction amount in milliunits format  # noqa: E501

        :param amount: The amount of this ScheduledTransactionSummary.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def memo(self):
        """Gets the memo of this ScheduledTransactionSummary.  # noqa: E501


        :return: The memo of this ScheduledTransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this ScheduledTransactionSummary.


        :param memo: The memo of this ScheduledTransactionSummary.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def flag_color(self):
        """Gets the flag_color of this ScheduledTransactionSummary.  # noqa: E501

        The scheduled transaction flag  # noqa: E501

        :return: The flag_color of this ScheduledTransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._flag_color

    @flag_color.setter
    def flag_color(self, flag_color):
        """Sets the flag_color of this ScheduledTransactionSummary.

        The scheduled transaction flag  # noqa: E501

        :param flag_color: The flag_color of this ScheduledTransactionSummary.  # noqa: E501
        :type: str
        """
        allowed_values = ["red", "orange", "yellow", "green", "blue", "purple"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and flag_color not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `flag_color` ({0}), must be one of {1}"  # noqa: E501
                .format(flag_color, allowed_values)
            )

        self._flag_color = flag_color

    @property
    def account_id(self):
        """Gets the account_id of this ScheduledTransactionSummary.  # noqa: E501


        :return: The account_id of this ScheduledTransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ScheduledTransactionSummary.


        :param account_id: The account_id of this ScheduledTransactionSummary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def payee_id(self):
        """Gets the payee_id of this ScheduledTransactionSummary.  # noqa: E501


        :return: The payee_id of this ScheduledTransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this ScheduledTransactionSummary.


        :param payee_id: The payee_id of this ScheduledTransactionSummary.  # noqa: E501
        :type: str
        """

        self._payee_id = payee_id

    @property
    def category_id(self):
        """Gets the category_id of this ScheduledTransactionSummary.  # noqa: E501


        :return: The category_id of this ScheduledTransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ScheduledTransactionSummary.


        :param category_id: The category_id of this ScheduledTransactionSummary.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def transfer_account_id(self):
        """Gets the transfer_account_id of this ScheduledTransactionSummary.  # noqa: E501

        If a transfer, the account_id which the scheduled transaction transfers to  # noqa: E501

        :return: The transfer_account_id of this ScheduledTransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._transfer_account_id

    @transfer_account_id.setter
    def transfer_account_id(self, transfer_account_id):
        """Sets the transfer_account_id of this ScheduledTransactionSummary.

        If a transfer, the account_id which the scheduled transaction transfers to  # noqa: E501

        :param transfer_account_id: The transfer_account_id of this ScheduledTransactionSummary.  # noqa: E501
        :type: str
        """

        self._transfer_account_id = transfer_account_id

    @property
    def deleted(self):
        """Gets the deleted of this ScheduledTransactionSummary.  # noqa: E501

        Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests.  # noqa: E501

        :return: The deleted of this ScheduledTransactionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ScheduledTransactionSummary.

        Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests.  # noqa: E501

        :param deleted: The deleted of this ScheduledTransactionSummary.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and deleted is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted

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
        if not isinstance(other, ScheduledTransactionSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduledTransactionSummary):
            return True

        return self.to_dict() != other.to_dict()
