#!/usr/bin/env python3

import connexion
import os

from swagger_server import encoder
from swagger_server.database.config import configure_database, update_yaml_config_with_env


def main():
    update_yaml_config_with_env()
    app = connexion.App('resource_access_service', specification_dir='./swagger_server/swagger/')
    configure_database(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'resource-access-service'}, pythonic_params=True)
    
    port = int(os.environ.get("PORT", default=8080))
    app.run(port=port)


if __name__ == '__main__':
    main()
