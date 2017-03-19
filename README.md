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

## Configuration

TBD
