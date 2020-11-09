# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ApiError(Model):
    """
    desc: ApiError is returned according to the swagger doc when the server runs into an error while handling a request
    author: Luca Mueller
    date: 2020-11-09
    """

    def __init__(self, detail: str=None, status: int=None, title: str=None, type: str=None):  # noqa: E501
        """ApiError - a model defined in Swagger

        :param detail: The detail of this ApiError.  # noqa: E501
        :type detail: str
        :param status: The status of this ApiError.  # noqa: E501
        :type status: int
        :param title: The title of this ApiError.  # noqa: E501
        :type title: str
        :param type: The type of this ApiError.  # noqa: E501
        :type type: str
        """
        self.swagger_types = {
            'detail': str,
            'status': int,
            'title': str,
            'type': str
        }

        self.attribute_map = {
            'detail': 'detail',
            'status': 'status',
            'title': 'title',
            'type': 'type'
        }

        self._detail = detail
        self._status = status
        self._title = title
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'ApiError':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ApiError of this ApiError.  # noqa: E501
        :rtype: ApiError
        """
        return util.deserialize_model(dikt, cls)

    @property
    def detail(self) -> str:
        """Gets the detail of this ApiError.


        :return: The detail of this ApiError.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail: str):
        """Sets the detail of this ApiError.


        :param detail: The detail of this ApiError.
        :type detail: str
        """

        self._detail = detail

    @property
    def status(self) -> int:
        """Gets the status of this ApiError.


        :return: The status of this ApiError.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this ApiError.


        :param status: The status of this ApiError.
        :type status: int
        """

        self._status = status

    @property
    def title(self) -> str:
        """Gets the title of this ApiError.


        :return: The title of this ApiError.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this ApiError.


        :param title: The title of this ApiError.
        :type title: str
        """

        self._title = title

    @property
    def type(self) -> str:
        """Gets the type of this ApiError.


        :return: The type of this ApiError.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ApiError.


        :param type: The type of this ApiError.
        :type type: str
        """

        self._type = type
