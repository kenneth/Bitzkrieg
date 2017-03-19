# Bitzkrieg

## Objective

The project is a lightweight automatic trading system on cryptocurrency. 
It aims to access most actively trading exchange and manage the orders and trades.

## Installation

1. Build from source

Clone the project and go to the project directory. Run the following command.

```
pip install .
```

If you made any code change on the project and reinstall again, run the following command.

```
pip install --upgrade .
```

2. PyPI

You can get the build package from PyPI directly.

```
pip install bitzkrieg
```

Note: Currently the beta version has not been put to PyPI.

## Functionality

1. Single market making

First, set up the configuration same as [config.ini](config.ini).

Run the command

```
smm -config <your config file>
```

2. Gateway dependent

For each gateway it supports the following functionalities without the order server.

- Mass order cancel
    
    ```
        <gateway> -cancel -public <api public key> -private <api private key>
    ```
    
- Mass order status
    
    ```
        <gateway> -orders -public <api public key> -private <api private key>
    ```
    
- Balance
    
    ```
        <gateway> -balance -public <api public key> -private <api private key>
    ```

## Gateway

Currently the below gateways are supported:

- Gatecoin

## Database

Currently, it is supported to store the request and response messages into a [Redis](https://redis.io/) database. The requests and responses are stored into the same database but different indexes.

The requests are stored with request ID (e.g. ClOrdID) as the key and the FIX message as the value.

The responses are stored with execution ID (e.g. ExecID) as the key and the FIX message as the value.

## Market Data Feed

Currently, it is supported to receive the market data feed from [BitcoinExchangeFH](https://github.com/gavincyi/BitcoinExchangeFH). 

## Configuration

The configuration file contains the setup parameters of market data feed, database and gateways.

| Section | Item | Description |
| --- | --- | --- |
|**Database**|Port|The port of the Redis database.|
| |Request|The database index of the requests.|
| |Response|The database index of the responses.|
|**MarketFeed**|Host|The host of the market data feed, in format of "address:port".|
|**Gatecoin**|public|Your public key provided by Gatecoin.|
| |private|Your private key provided by Gatecoin.|

## Contact

If you have any inquires, please contact gavincyi at gmail dot com.
