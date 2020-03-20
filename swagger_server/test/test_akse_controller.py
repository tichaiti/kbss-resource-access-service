# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.resource_ref import ResourceRef  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAkseController(BaseTestCase):
    """AkseController integration test stubs"""

    def test_add_resource_access_for_user(self):
        """Test case for add_resource_access_for_user

        Gives user access to a resource
        """
        body = ResourceRef()
        response = self.client.open(
            '/api/resource/access/{dataType}/{userId}'.format(data_type='data_type_example', user_id='user_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_resource_access_for_user(self):
        """Test case for get_resource_access_for_user

        Gets resource user has access to
        """
        response = self.client.open(
            '/api/resource/access/{dataType}/{userId}'.format(data_type='data_type_example', user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
