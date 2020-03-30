import os

from connexion import FlaskApp
from flask_restplus_data import FlaskData

from swagger_server import resources
from swagger_server.resources import migrations

flask_data = FlaskData(os.path.dirname(resources.__file__))


def configure_database(app: FlaskApp):
    global flask_data
    flask_data.initialize(app)
    database_url = os.environ.get('DATABASE_URL', None)
    if database_url is not None:
        flask_data.url = database_url
    flask_data.migration_directory = os.path.dirname(migrations.__file__)
