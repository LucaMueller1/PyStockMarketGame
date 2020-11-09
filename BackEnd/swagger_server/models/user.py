# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """
    desc: User contains all the necessary information to describe a user
    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, id: int=None, first_name: str=None, last_name: str=None, email: str=None, password: str=None, starting_capital: float=None, money_available: float=None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: int
        :param first_name: The first_name of this User.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this User.  # noqa: E501
        :type last_name: str
        :param email: The email of this User.  # noqa: E501
        :type email: str
        :param password: The password of this User.  # noqa: E501
        :type password: str
        :param starting_capital: The starting_capital of this User.  # noqa: E501
        :type starting_capital: float
        :param money_available: The money_available of this User.  # noqa: E501
        :type money_available: float
        """
        self.swagger_types = {
            'id': int,
            'first_name': str,
            'last_name': str,
            'email': str,
            'password': str,
            'starting_capital': float,
            'money_available': float
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email': 'email',
            'password': 'password',
            'starting_capital': 'startingCapital',
            'money_available': 'moneyAvailable'
        }

        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._starting_capital = starting_capital
        self._money_available = money_available

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: int
        """

        self._id = id

    @property
    def first_name(self) -> str:
        """Gets the first_name of this User.


        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this User.


        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def email(self) -> str:
        """Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this User.


        :param email: The email of this User.
        :type email: str
        """

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this User.


        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this User.


        :param password: The password of this User.
        :type password: str
        """

        self._password = password

    @property
    def starting_capital(self) -> float:
        """Gets the starting_capital of this User.


        :return: The starting_capital of this User.
        :rtype: float
        """
        return self._starting_capital

    @starting_capital.setter
    def starting_capital(self, starting_capital: float):
        """Sets the starting_capital of this User.


        :param starting_capital: The starting_capital of this User.
        :type starting_capital: float
        """

        self._starting_capital = starting_capital

    @property
    def money_available(self) -> float:
        """Gets the money_available of this User.


        :return: The money_available of this User.
        :rtype: float
        """
        return self._money_available

    @money_available.setter
    def money_available(self, money_available: float):
        """Sets the money_available of this User.


        :param money_available: The money_available of this User.
        :type money_available: float
        """

        self._money_available = money_available
