from typing import List
from flask_restplus_data import FlaskDataRepository, Query
from swagger_server.database.config import flask_data


class ResourceAccessModel(flask_data.Model):

    __tablename__ = 'resource_access'

    id = flask_data.Id(flask_data.db.Integer)
    user_id = flask_data.String()
    resource_id = flask_data.String()
    resource_type = flask_data.String()

    def __init__(self, user_id: str, resource_id: str, resource_type: str) -> None:
        self.user_id = user_id
        self.resource_id = resource_id
        self.resource_type = resource_type


@FlaskDataRepository
class ResourceRepository:
    @Query('SELECT * FROM resource_access WHERE user_id = :user_id AND resource_type = :data_type')
    def get_resource_access_for_user(self, user_id: str, data_type: str) -> List[ResourceAccessModel]:
        pass
