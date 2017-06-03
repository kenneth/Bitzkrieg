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
    parser = argparse.ArgumentParser(description='Single market marking.')
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
    logger.info('[main]', "Process is starting now...")

    # Initialize objects
    market_data_feed = factory.create_market_data_feed(logger)
    journal_db = factory.create_journal_database()
    realtime_db = factory.create_realtime_database()
    risk_manager = factory.create_risk_manager()
    order_server = factory.create_order_server(logger, journal_db, realtime_db, risk_manager, market_data_feed)
    instmt_list = factory.create_instrument_list()

    # Register exchange
    for exchange_name in ['Gatecoin']:
        exchange_gateway = factory.create_exchange('Gatecoin', logger, market_data_feed=market_data_feed)
        order_server.register_exchange(exchange_gateway)

    # Initialize exchange risk
    order_server.initialize_exchange_risk()

    # Strategy initialization
    strategies = factory.create_strategies(order_server, logger, instmt_list)

    # Start the strategies
    for strategy in strategies:
        logger.info('[main]', 'Initializing strategy (%s)...' % strategy.get_name())
        strategy.init_strategy()

    while True:
        snapshot = order_server.get_latest_snapshot(200000)
        strategies = [strategy for strategy in strategies if strategy.on_market_update(snapshot)]
        if len(strategies) == 0:
            logger.info('[main]', "All strategies has returned safely.")
            break

    # Starting...
    logger.info('[main]', "Process has ended.")

if __name__ == '__main__':
    main()

