#!/usr/bin/env python3
"""
desc: Main is used to configure and run the Flask/Connexion Server
author: Luca Mueller
date: 2020-11-07
"""

import connexion
from apscheduler.schedulers.background import BackgroundScheduler

from swagger_server import encoder
from swagger_server.services.schedule_service import insert_stock_data


def main():
    start_scheduler()
    app = connexion.App(__name__, specification_dir='swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'PyBroker'})
    app.run(port=8080)


def start_scheduler():
    """

        desc: Function to start the Scheduler for the periodic insertion of the Stock Prices

        param: None

    """
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(insert_stock_data, 'interval', minutes=15)
    sched.start()


if __name__ == '__main__':
    main()
