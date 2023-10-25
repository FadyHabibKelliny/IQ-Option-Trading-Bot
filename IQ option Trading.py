import talib
import requests
import time
from iqoptionapi.stable_api import IQ_Option
import numpy as np

# Replace with your IQ Option email and password
API = IQ_Option('your_email@email.com','Password')
API.connect()

# Replace with the amount you want to trade
amount = 10

# Define the account type to demo (virtual) or real
demo_account = True

# Login to the selected account type
if demo_account:
    API.change_balance("PRACTICE")
else:
    API.change_balance("REAL")

while True:
    try:
        # Check if the API connection is still alive
        if not API.check_connect():
            print("API connection lost, attempting to reconnect...")
            API.connect()
            # Login to the selected account type after reconnecting
            if demo_account:
                API.change_balance("PRACTICE")
            else:
                API.change_balance("REAL")
        
        # Get the current account balance
        balance = API.get_balance()
        print(f"Current balance: {balance}")
        
        # Get information about market opening times for all assets
        open_times = API.get_all_open_time()
        
        # Loop through the list of opening times to find the first open asset
        symbol = None
        for asset in open_times["turbo"]:
            if open_times["turbo"][asset]["open"]:
                symbol = asset
                break
        
        if symbol is None:
            print("No assets are currently open")
            time.sleep(60)
            continue
        
        print(f"Trading {symbol}")
        
        # Get the RSI indicator value for the last 14 candles
        candles = API.get_candles(symbol,60,111, time.time())
        close_prices = [candle["close"] for candle in candles]
        close_prices = np.array(close_prices)  # Convert list to numpy array
        rsi = talib.RSI(close_prices)

        print(f"Current RSI: {rsi[-1]}")

        # If the RSI is below 30 and the account balance is sufficient, place a call option
        if rsi[-1] < 36 and balance >= amount:
            buy_option = API.buy(1, symbol, 'CALL', amount)
            print("Call option placed")
            print(API.check_win(buy_option[1]))
            print(API.check_win(id))

        # If the RSI is above 70 and the account balance is sufficient, place a put option
        elif rsi[-1] > 59.8 and balance >= amount:
            buy_option = API.buy(1, symbol, 'PUT', amount)
            print("Put option placed")
            print(API.check_win(buy_option[1]))
            print(API.check_win(id))

        # Wait for 1 minute before checking again
        time.sleep(60)
    except (requests.exceptions.HTTPError, ConnectionError, TimeoutError):
        print("Error: Connection lost, attempting to reconnect...")
        time.sleep(5)
        continue
