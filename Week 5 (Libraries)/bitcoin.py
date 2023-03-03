"""
Task:
In a file called bitcoin.py, implement a program that:

    - Expects the user to specify as a command-line argument the number of Bitcoins,N , that they would like to buy. If that argument cannot 
    be converted to a float, the program should exit via sys.exit with an error message.
    
    - Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, 
    among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions.
    
    - Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.
"""

import requests
import sys

def main():
    coins = get_coins()
    price = get_price()
    total = coins * price
    print(f"${total:,.4f}")




def get_coins():
    try:
        coins = float(sys.argv[1])
        return coins
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

def get_price():
    try:
        price_req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        price = price_req.json()["bpi"]["USD"]["rate_float"]
        return price

    except requests.RequestException:
        pass


if __name__ == "__main__":
    main()
