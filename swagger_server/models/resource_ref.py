# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResourceRef(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ids: List[str]=None):  # noqa: E501
        """ResourceRef - a model defined in Swagger

        :param ids: The ids of this ResourceRef.  # noqa: E501
        :type ids: List[str]
        """
        self.swagger_types = {
            'ids': List[str]
        }

        self.attribute_map = {
            'ids': 'ids'
        }
        self._ids = ids

    @classmethod
    def from_dict(cls, dikt) -> 'ResourceRef':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResourceRef of this ResourceRef.  # noqa: E501
        :rtype: ResourceRef
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ids(self) -> List[str]:
        """Gets the ids of this ResourceRef.


        :return: The ids of this ResourceRef.
        :rtype: List[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids: List[str]):
        """Sets the ids of this ResourceRef.


        :param ids: The ids of this ResourceRef.
        :type ids: List[str]
        """

        self._ids = ids
