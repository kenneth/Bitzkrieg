#!/bin/python
from bitz.factory import Factory
import argparse

try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

def get_args():
    """
    Get input arguments
    """
    parser = argparse.ArgumentParser(description='Account balance archive.')
    parser.add_argument('-config', action='store', dest='config',
                        help='Configuration file path',
                        default='')
    return parser.parse_args()

def main():
    # Get input arguments
    args = get_args()

    # Create factory
    factory = Factory(args.config)

    # Logger
    logger = factory.create_logger()

    # Starting...
    logger.info('[main]', "Start to archive account balance...")

    # Initialize objects
    journal_db = factory.create_journal_database()
    realtime_db = factory.create_realtime_database()
    order_server = factory.create_order_server(logger, journal_db, realtime_db, None, None)

    # Initialize exchange risk
    order_server.initialize_exchange_risk()

    logger.info('[main]', "Finished to archive account balance.")

if __name__ == '__main__':
    main()
