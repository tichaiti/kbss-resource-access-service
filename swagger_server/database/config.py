import os
import yaml

from connexion import FlaskApp
from flask_restplus_data import FlaskData
from jsonpath_ng import jsonpath, parse

from swagger_server import resources
from swagger_server.resources import migrations

flask_data = FlaskData(os.path.dirname(resources.__file__))


def override_with_env(config):
    for key, val in os.environ.items():
        path = f'$.{key.lower().replace("_", ".")}'
        jsonpath_expr = parse(path)
        jsonpath_expr.find(config)
        jsonpath_expr.update(config, val)


def update_yaml_config_with_env():
    with open(os.path.join(os.path.dirname(resources.__file__), 'config.yaml'), 'r+') as config_file:
        config = yaml.load(config_file)
        override_with_env(config)
        config_file.seek(0)
        yaml.dump(config, config_file)


def configure_database(app: FlaskApp):
    global flask_data
    flask_data.initialize(app)
    database_url = os.environ.get('DATABASE_URL', None)
    if database_url is not None:
        flask_data.url = database_url
    flask_data.migration_directory = os.path.dirname(migrations.__file__)
