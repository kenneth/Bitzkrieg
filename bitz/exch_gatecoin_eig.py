#!/usr/bin/python3  
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
                 key,
                 secret,
                 api_url = "https://api.gatecoin.com/"):
        """
        Constructor
        
        :param key          Public key
        :param secret       Private key
        :param api_url      API URL
        """
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
        
        data = None
        
        if httpMethod == "DELETE":
          R = requests.delete
        elif httpMethod == "GET":
          R = requests.get
        elif httpMethod == "POST":
          R = requests.post     
          
        data = json.dumps(params)
        response = R(url, data=data, headers=headers)
        
        return response.json()
    
    def check_success(self, msg):
        return 'responseStatus' in msg and \
               'message' in msg['responseStatus'] and \
               msg['responseStatus']['message'] == 'OK'
        
if __name__ == '__main__':
    # Run "curl icanhazip.com" to get the outgoing IP before generating the key pair.
    
    key = input("What is the public key? ")
    secret = input("What is the private key? ")
    gw = GatecoinEig(key, secret)
    ret = gw.send_request("Balance/Balances", "GET")
    print(ret)
    print(gw.check_success(ret))

        
    
    
    