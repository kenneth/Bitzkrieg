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

1. Trading application

First, set up the configuration same as [config.ini](config.ini).

Run the command

```
bitz -config <your config file>
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

## Market Data Feed

Currently, it is supported to receive the market data feed from [BitcoinExchangeFH](https://github.com/gavincyi/BitcoinExchangeFH). 

## Configuration

The configuration file contains the setup parameters of market data feed, database and gateways.

| Section | Item | Description |
| --- | --- | --- |
|**MarketFeed**|Type=file|For backtesting use. Market data sourced from files.|
||Files|List of file names.|
||Type=bcfh|Bitcoinexchange feed handler.|
||Host|ZeroMQ host, e.g. "tcp://localhost:6001"|
|**JournalDatabase**|Type=Internal|Internal memory cache.|
||Path|Output file path when the process exits cleanly.|
|**RealtimeDatabase**|Type=Internal|Internal memory cache.|
||Path|Output file path when the process exits cleanly.|
||Type=Sqlite|Sqlite database. Updated in real time.|
||Path|Output file path when the process exits cleanly.|
|**Instrument.**||Unique name for the instrument section. Prefix of "Instrument."|
||Exchange|Exchange name.|
||Name|Instrument name.|
||USDRate|USD rate.|
||PriceMinSize|Price minimum size, e.g. 0.01|
||QtyMinSize|Quantity minimum size, e.g. 0.000001|

## Contact

If you have any inquires, please contact gavincyi at gmail dot com.
