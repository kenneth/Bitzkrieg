#!/usr/bin/python3
import signal

class RealTimeStrategy:
    """
    Real time strategy.

    The strategy handles the following:
    1. Subscribe the market data feed
    2. Manage the exchange price depth and trades
    3. Trigger orders to order server
    4. Maintain orders
    5. Risk management
    """
    def __init__(self, name, ordsvr, logger):
        """
        Constructor
        """
        self.name = name                # Strategy name
        self.ordsvr = ordsvr      # Order server
        self.logger = logger            # Logger
        self.market_data_feed = None    # Market data feed
        self.running = True
        self.max_fiat_currency_risk = None

    def get_name(self):
        """
        Get name
        """
        return self.name

    def init_strategy(self):
        """
        Initialize strategy. Called before getting market data.
        """
        raise NotImplementedError("Not implemented for strategy (%s)." % self.get_name())

    def on_market_update(self, snapshot):
        """
        Callback when the market is updated.
        :param snapshot: Market data snapshot
        :return False for terminating running
        """
        raise NotImplementedError("Not implemented for strategy (%s)." % self.get_name())

    def handle_signal(self, sig, stack):
        """
        Handle the signal received for the process
        """
        if sig == signal.SIGINT or sig == signal.SIGTERM:
            self.running = False
            self.logger.info(self.__class__.__name__, \
                    "Stack (%s) is received. Strategy %s is exiting..." % (stack, self.name))
        else:
            assert False, "Unrecognized signal %d" % sig




