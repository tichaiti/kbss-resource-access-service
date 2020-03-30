#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server.database.config import configure_database


def main():
    app = connexion.App('resource_access_service', specification_dir='./swagger/')
    configure_database(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'resource-access-service'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
