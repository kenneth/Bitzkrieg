#!/bin/python
import requests
import json
from time import time
class RestApiConnector(object):
    """
    REST API connector
    """
    class HTTPMethod:
        GET = 0,
        DELETE = 1,
        POST = 2

        @classmethod
        def str(cls, value):
            if value == RestApiConnector.HTTPMethod.GET:
                return 'GET'
            elif value == RestApiConnector.HTTPMethod.DELETE:
                return 'DELETE'
            elif value == RestApiConnector.HTTPMethod.POST:
                return 'POST'
            else:
                raise NotImplementedError("Not implemented value %s" % value)

    def __init__(self, logger, public_key, private_key, url):
        """
        Constructor
        """
        self.logger = logger
        self.url = url
        self._public_key = public_key
        self._private_key = private_key

    @classmethod
    def generate_nonce(cls):
        """
        Generate an increasing unique number
        """
        return int(round(time() * 1000))

    def generate_headers(self):
        """
        Generate headers
        """
        raise NotImplementedError("Not yet implemented.")

    def generate_auth(self):
        """
        Generate authentication
        """
        raise NotImplementedError("Not yet implemented.")

    def send_request(self, command, httpMethod: HTTPMethod, params=None):
        """
        Send request
        :param command: API command
        :param httpMethod: Http method
        :param params: input parameters
        :return: JSON object
        """
        url = self.url + command
        headers = self.generate_headers()
        auth = self.generate_auth()
        data = "" if params is None else json.dumps(params)

        if httpMethod == RestApiConnector.HTTPMethod.DELETE:
            R = requests.delete
        elif httpMethod == RestApiConnector.HTTPMethod.GET:
            R = requests.get
        elif httpMethod == RestApiConnector.HTTPMethod.POST:
            R = requests.post

        self.logger.info(self.__class__.__name__, 'OUT\nmethod=%s\nurl=%s\ndata=%s\nheaders=%s\n' % \
                         (RestApiConnector.HTTPMethod.str(httpMethod), url, data, headers))
        try:
            if auth is None:
                response = R(url, data=data, headers=headers)
            else:
                response = R(url, data=data, headers=headers, auth=auth)

            self.logger.info(self.__class__.__name__, 'IN (%d)\n%s' % (response.status_code, response.text))
            return response
        except Exception as e:
            return e

    def get_public_key(self):
        """
        Access public key
        """
        return self._public_key

