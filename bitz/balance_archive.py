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
    instmt_list = factory.create_instrument_list()
    journal_db = factory.create_journal_database()
    realtime_db = factory.create_realtime_database()
    risk_manager = factory.create_risk_manager(instmt_list)
    market_data_feed = factory.create_market_data_feed(logger, is_basic=True)
    order_server = factory.create_order_server(logger, journal_db, realtime_db, risk_manager, market_data_feed, instmt_list)
    factory.create_exchanges(logger, order_server, market_data_feed)

    # Initialize exchange risk
    order_server.initialize_exchange_risk()

    # Initialize exchange positions
    order_server.initialize_exchange_positions()

    logger.info('[main]', "Finished to archive account balance.")

if __name__ == '__main__':
    main()
