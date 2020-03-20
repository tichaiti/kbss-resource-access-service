import connexion
import six

from swagger_server.models.resource_access import ResourceAccess  # noqa: E501
from swagger_server.models.resource_ref import ResourceRef  # noqa: E501
from swagger_server import util


def add_resource_access_for_user(body, data_type, user_id):  # noqa: E501
    """Gives user access to a resource

    Adds a resource id to user access list # noqa: E501

    :param body: The resource id.
    :type body: dict | bytes
    :param data_type: The data type ex book.
    :type data_type: str
    :param user_id: The user id
    :type user_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = ResourceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_resource_access_for_user(data_type, user_id):  # noqa: E501
    """Gets resource user has access to

    Returns list of ids of DataType user has access to # noqa: E501

    :param data_type: The data type ex book.
    :type data_type: str
    :param user_id: The user id
    :type user_id: str

    :rtype: ResourceAccess
    """
    return 'do some magic!'
