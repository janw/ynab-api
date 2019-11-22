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


class ScheduledSubTransaction(object):
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
        'scheduled_transaction_id': 'str',
        'amount': 'int',
        'memo': 'str',
        'payee_id': 'str',
        'category_id': 'str',
        'transfer_account_id': 'str',
        'deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'scheduled_transaction_id': 'scheduled_transaction_id',
        'amount': 'amount',
        'memo': 'memo',
        'payee_id': 'payee_id',
        'category_id': 'category_id',
        'transfer_account_id': 'transfer_account_id',
        'deleted': 'deleted'
    }

    def __init__(self, id=None, scheduled_transaction_id=None, amount=None, memo=None, payee_id=None, category_id=None, transfer_account_id=None, deleted=None, local_vars_configuration=None):  # noqa: E501
        """ScheduledSubTransaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._scheduled_transaction_id = None
        self._amount = None
        self._memo = None
        self._payee_id = None
        self._category_id = None
        self._transfer_account_id = None
        self._deleted = None
        self.discriminator = None

        self.id = id
        self.scheduled_transaction_id = scheduled_transaction_id
        self.amount = amount
        if memo is not None:
            self.memo = memo
        if payee_id is not None:
            self.payee_id = payee_id
        if category_id is not None:
            self.category_id = category_id
        if transfer_account_id is not None:
            self.transfer_account_id = transfer_account_id
        self.deleted = deleted

    @property
    def id(self):
        """Gets the id of this ScheduledSubTransaction.  # noqa: E501


        :return: The id of this ScheduledSubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScheduledSubTransaction.


        :param id: The id of this ScheduledSubTransaction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def scheduled_transaction_id(self):
        """Gets the scheduled_transaction_id of this ScheduledSubTransaction.  # noqa: E501


        :return: The scheduled_transaction_id of this ScheduledSubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_transaction_id

    @scheduled_transaction_id.setter
    def scheduled_transaction_id(self, scheduled_transaction_id):
        """Sets the scheduled_transaction_id of this ScheduledSubTransaction.


        :param scheduled_transaction_id: The scheduled_transaction_id of this ScheduledSubTransaction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and scheduled_transaction_id is None:  # noqa: E501
            raise ValueError("Invalid value for `scheduled_transaction_id`, must not be `None`")  # noqa: E501

        self._scheduled_transaction_id = scheduled_transaction_id

    @property
    def amount(self):
        """Gets the amount of this ScheduledSubTransaction.  # noqa: E501

        The scheduled subtransaction amount in milliunits format  # noqa: E501

        :return: The amount of this ScheduledSubTransaction.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ScheduledSubTransaction.

        The scheduled subtransaction amount in milliunits format  # noqa: E501

        :param amount: The amount of this ScheduledSubTransaction.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def memo(self):
        """Gets the memo of this ScheduledSubTransaction.  # noqa: E501


        :return: The memo of this ScheduledSubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this ScheduledSubTransaction.


        :param memo: The memo of this ScheduledSubTransaction.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def payee_id(self):
        """Gets the payee_id of this ScheduledSubTransaction.  # noqa: E501


        :return: The payee_id of this ScheduledSubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this ScheduledSubTransaction.


        :param payee_id: The payee_id of this ScheduledSubTransaction.  # noqa: E501
        :type: str
        """

        self._payee_id = payee_id

    @property
    def category_id(self):
        """Gets the category_id of this ScheduledSubTransaction.  # noqa: E501


        :return: The category_id of this ScheduledSubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ScheduledSubTransaction.


        :param category_id: The category_id of this ScheduledSubTransaction.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def transfer_account_id(self):
        """Gets the transfer_account_id of this ScheduledSubTransaction.  # noqa: E501

        If a transfer, the account_id which the scheduled subtransaction transfers to  # noqa: E501

        :return: The transfer_account_id of this ScheduledSubTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transfer_account_id

    @transfer_account_id.setter
    def transfer_account_id(self, transfer_account_id):
        """Sets the transfer_account_id of this ScheduledSubTransaction.

        If a transfer, the account_id which the scheduled subtransaction transfers to  # noqa: E501

        :param transfer_account_id: The transfer_account_id of this ScheduledSubTransaction.  # noqa: E501
        :type: str
        """

        self._transfer_account_id = transfer_account_id

    @property
    def deleted(self):
        """Gets the deleted of this ScheduledSubTransaction.  # noqa: E501

        Whether or not the scheduled subtransaction has been deleted.  Deleted scheduled subtransactions will only be included in delta requests.  # noqa: E501

        :return: The deleted of this ScheduledSubTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ScheduledSubTransaction.

        Whether or not the scheduled subtransaction has been deleted.  Deleted scheduled subtransactions will only be included in delta requests.  # noqa: E501

        :param deleted: The deleted of this ScheduledSubTransaction.  # noqa: E501
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
        if not isinstance(other, ScheduledSubTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduledSubTransaction):
            return True

        return self.to_dict() != other.to_dict()
