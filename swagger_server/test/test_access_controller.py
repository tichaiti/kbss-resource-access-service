# coding: utf-8

from __future__ import absolute_import

from unittest.mock import MagicMock, PropertyMock

import flask_restplus_data
from flask import json
from flask_restplus_data import FlaskData
from flask_restplus_data.enum import DatabaseType
from flask_sqlalchemy import Model
from six import BytesIO

from swagger_server.database import config
from swagger_server.models.resource_ref import ResourceRef  # noqa: E501
from swagger_server.test import BaseTestCase

config.flask_data = MagicMock()
config.flask_data.Model = object
flask_restplus_data.FlaskDataRepository = MagicMock()


class TestAccessController(BaseTestCase):
    """AccessController integration test stubs"""

    def test_add_resource_access_for_user(self):
        """Test case for add_resource_access_for_user

        Gives user access to a resource
        """
        body = ResourceRef(ids=["1", "2", "3"])
        response = self.client.open(
            '/api/resource/access/{data_type}/{user_id}'.format(data_type='book', user_id='user_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assertStatus(response, 204,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_resource_access_for_user(self):
        """Test case for get_resource_access_for_user

        Gets resource user has access to
        """
        response = self.client.open(
            '/api/resource/access/{data_type}/{user_id}'.format(data_type='book', user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
