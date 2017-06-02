#!/usr/bin/python3  
from bitz.logger import ConsoleLogger
import time
import base64
import hmac
import urllib
import requests
import hashlib
import json

class ExchGatecoinEig(object):
    """
    Exchange interface gateway
    """
    
    def __init__(self,
                 logger,
                 key,
                 secret,
                 api_url = "https://api.gatecoin.com/"):
        """
        Constructor
        
        :param key          Public key
        :param secret       Private key
        :param api_url      API URL
        """
        self.logger = logger
        self.key = key
        self.secret = secret
        self.api_url = api_url
        
    def send_request(self, command, httpMethod, params={}):
        now = str(time.time())
        contentType = "" if httpMethod == "GET" else "application/json"
        
        url = self.api_url + command
        
        message = httpMethod + url + contentType + now
        message = message.lower()
        
        signature = hmac.new(self.secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).digest()
        hashInBase64 = base64.b64encode(signature, altchars=None)
        
        headers = {
        'API_PUBLIC_KEY': self.key,
        'API_REQUEST_SIGNATURE': hashInBase64,
        'API_REQUEST_DATE': now,
        'Content-Type':'application/json'
        }
        
        if httpMethod == "DELETE":
          R = requests.delete
        elif httpMethod == "GET":
          R = requests.get
        elif httpMethod == "POST":
          R = requests.post     
          
        data = json.dumps(params)
        self.logger.info('OUT', 'method=%s\nurl=%s\ndata=%s\nheaders=%s\n' % \
                                    (httpMethod, url, data, headers))
        try:
            response = R(url, data=data, headers=headers)
            if response.status_code == 200:
                response = response.json()
            else:
                response = {'failed_code': response.status_code, 'failed_text': response.text}
            self.logger.info('IN', response)
        except Exception as e:
            response = { 'failed_code': 999, 'failed_text': str(e)[:100]}

        return response
    
    def check_success(self, msg):
        return 'responseStatus' in msg and \
               'message' in msg['responseStatus'] and \
               msg['responseStatus']['message'] == 'OK'
        
if __name__ == '__main__':
    # Run "curl icanhazip.com" to get the outgoing IP before generating the key pair.
    
    key = input("What is the public key? ")
    secret = input("What is the private key? ")
    gw = ExchGatecoinEig(ConsoleLogger.static_logger, key, secret)
    ret = gw.send_request("Balance/Balances", "GET")
    print(ret)
    print(gw.check_success(ret))

        
    
    
    