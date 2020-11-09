# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AuthKey(Model):
    """
    desc: AuthKey is used to authenticate the user to use request in his session
    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, user_id: int=None, auth_key: str=None, expiry: datetime=None):  # noqa: E501
        """AuthKey - a model defined in Swagger

        :param user_id: The user_id of this AuthKey.  # noqa: E501
        :type user_id: int
        :param auth_key: The auth_key of this AuthKey.  # noqa: E501
        :type auth_key: str
        :param expiry: The expiry of this AuthKey.  # noqa: E501
        :type expiry: datetime
        """
        self.swagger_types = {
            'user_id': int,
            'auth_key': str,
            'expiry': datetime
        }

        self.attribute_map = {
            'user_id': 'userId',
            'auth_key': 'authKey',
            'expiry': 'expiry'
        }

        self._user_id = user_id
        self._auth_key = auth_key
        self._expiry = expiry

    @classmethod
    def from_dict(cls, dikt) -> 'AuthKey':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AuthKey of this AuthKey.  # noqa: E501
        :rtype: AuthKey
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> int:
        """Gets the user_id of this AuthKey.


        :return: The user_id of this AuthKey.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this AuthKey.


        :param user_id: The user_id of this AuthKey.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def auth_key(self) -> str:
        """Gets the auth_key of this AuthKey.


        :return: The auth_key of this AuthKey.
        :rtype: str
        """
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key: str):
        """Sets the auth_key of this AuthKey.


        :param auth_key: The auth_key of this AuthKey.
        :type auth_key: str
        """

        self._auth_key = auth_key

    @property
    def expiry(self) -> datetime:
        """Gets the expiry of this AuthKey.


        :return: The expiry of this AuthKey.
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry: datetime):
        """Sets the expiry of this AuthKey.


        :param expiry: The expiry of this AuthKey.
        :type expiry: datetime
        """

        self._expiry = expiry
