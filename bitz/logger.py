from datetime import datetime
import logging


class Logger:
    """
    Generic logger
    """
    def __init__(self, name, output=None):
        """
        Initialise the logger
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.ERROR)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s \n%(message)s\n')
        if output is None:
            slogger = logging.StreamHandler()
            slogger.setFormatter(formatter)
            self.logger.addHandler(slogger)
        else:
            flogger = logging.FileHandler(output)
            flogger.setFormatter(formatter)
            self.logger.addHandler(flogger)

    def info(self, method, str):
        """
        Write info log
        :param method: Method name
        :param str: Log message
        """
        self.logger.info('[%s]\n%s\n' % (method, str))

    def error(self, method, str):
        """
        Write info log
        :param method: Method name
        :param str: Log message
        """
        self.logger.error('[%s]\n%s\n' % (method, str))
        
        
class ConsoleLogger:
    static_logger = Logger('ConsoleLogger')
    
    @staticmethod
    def info(method, str):
        """
        Write info log
        :param method: Method name
        :param str: Log message
        """
        ConsoleLogger.static_logger.info(method, str)

    @staticmethod
    def error(method, str):
        """
        Write info log
        :param method: Method name
        :param str: Log message
        """
        ConsoleLogger.static_logger.error(method, str)