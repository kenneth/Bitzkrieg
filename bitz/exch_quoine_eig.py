#!/usr/bin/python3  
from bitz.logger import ConsoleLogger
import time
import base64
import hmac
import urllib
import requests
import hashlib
import json

class ExchQuoineEig(object):
    """
    Exchange interface gateway
    """
    
    def __init__(self,
                 logger,
                 key,
                 secret,
                 api_url = "https://api.quoine.com"):
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
        auth_payload = { "path": command,
                         "nonce": int(time.time() * 1000),
                         "token_id": self.key}
        signature = jwt.encode(auth_payload, self.secret, algorithm='HS256')
        headers = {
        'X-Quoine-API-Version': '2',
        'X-Quoine-Auth': signature,
        'Content-Type':'application/json'
        }
        
        data = None
        
        if httpMethod == "DELETE":
          R = requests.delete
        elif httpMethod == "GET":
          R = requests.get
        elif httpMethod == "POST":
          R = requests.post     
          
        data = json.dumps(params)
        self.logger.info('OUT', 'url=%s\ndata=%s\nheaders=%s\n' % \
                                    (url, data, headers))
        response = R(url, data=data, headers=headers)
        if response.status_code == 200:
            response = response.json()
        else:
            response = {'failed_code': response.status_code, 'failed_text': response.text}
        self.logger.info('IN', response)
        
        return response
    
    def check_success(self, msg):
        return 'responseStatus' in msg and \
               'message' in msg['responseStatus'] and \
               msg['responseStatus']['message'] == 'OK'
        
if __name__ == '__main__':
    # Run "curl icanhazip.com" to get the outgoing IP before generating the key pair.
    
    key = input("What is the public key? ")
    secret = input("What is the private key? ")
    gw = ExchQuoineEig(ConsoleLogger.static_logger, key, secret)
    ret = gw.send_request("/fiat_accounts", "GET")
    print(ret)
    print(gw.check_success(ret))

        
    
    
    