# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserPrepareLogin(Model):
    """
    desc: UserPrepareLogin contains all the necessary information to log in a user
    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, email: str=None, password: str=None):  # noqa: E501
        """UserPrepareLogin - a model defined in Swagger

        :param email: The email of this UserPrepareLogin.  # noqa: E501
        :type email: str
        :param password: The password of this UserPrepareLogin.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {
            'email': str,
            'password': str
        }

        self.attribute_map = {
            'email': 'email',
            'password': 'password'
        }

        self._email = email
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'UserPrepareLogin':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserPrepareLogin of this UserPrepareLogin.  # noqa: E501
        :rtype: UserPrepareLogin
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self) -> str:
        """Gets the email of this UserPrepareLogin.


        :return: The email of this UserPrepareLogin.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this UserPrepareLogin.


        :param email: The email of this UserPrepareLogin.
        :type email: str
        """

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this UserPrepareLogin.


        :return: The password of this UserPrepareLogin.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this UserPrepareLogin.


        :param password: The password of this UserPrepareLogin.
        :type password: str
        """

        self._password = password
