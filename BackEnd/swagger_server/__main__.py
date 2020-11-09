#!/usr/bin/env python3
"""
desc: Main is used to configure and run the Flask/Connexion Server
author: Luca Mueller
date: 2020-11-07
"""

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'PyBroker'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
