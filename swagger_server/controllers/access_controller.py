import connexion
import six
from werkzeug.exceptions import BadRequest

from swagger_server.database.ResourceAccess import ResourceRepository, ResourceAccessModel
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
    if not connexion.request.is_json:
        raise BadRequest('Only application/json supported.')
    resource_ref = ResourceRef.from_dict(connexion.request.get_json())
    with ResourceRepository(ResourceAccessModel) as repo:
        for resource_id in resource_ref.ids:
            resource_access = ResourceAccessModel(user_id, resource_id, data_type)
            repo.save(resource_access)


def get_resource_access_for_user(data_type, user_id):  # noqa: E501
    """Gets resource user has access to

    Returns list of ids of DataType user has access to # noqa: E501

    :param data_type: The data type ex book.
    :type data_type: str
    :param user_id: The user id
    :type user_id: str

    :rtype: ResourceAccess
    """
    with ResourceRepository(ResourceAccessModel) as repo:
        access_list = repo.get_resource_access_for_user(user_id, data_type)
    resource_ids = [access.resource_id for access in access_list]
    return ResourceAccess(count=len(resource_ids), data=resource_ids)
