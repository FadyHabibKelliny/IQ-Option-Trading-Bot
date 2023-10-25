import talib                # Import the talib library for technical analysis
import requests             # Import the requests library for making HTTP requests
import time                 # Import the time module for time-related functions
from iqoptionapi.stable_api import IQ_Option  # Import the IQ Option API
import numpy as np          # Import the NumPy library for numerical operations

# Replace with your IQ Option email and password
API = IQ_Option('your_email@email.com','Password')  # Initialize the IQ Option API with your credentials
API.connect()              # Connect to the IQ Option platform

# Replace with the amount you want to trade
amount = 10                # Set the amount to be traded

# Define the account type to demo (virtual) or real
demo_account = True        # Set whether the account is a demo (True) or real (False) account

# Login to the selected account type
if demo_account:
    API.change_balance("PRACTICE")  # If it's a demo account, change the balance to practice (virtual)
else:
    API.change_balance("REAL")      # If it's a real account, change the balance to real

while True:                 # Start an infinite loop for continuous trading
    try:
        # Check if the API connection is still alive
        if not API.check_connect():
            print("API connection lost, attempting to reconnect...")
            API.connect()       # If the connection is lost, attempt to reconnect
            # Login to the selected account type after reconnecting
            if demo_account:
                API.change_balance("PRACTICE")  # If it's a demo account, change the balance to practice (virtual) after reconnecting
            else:
                API.change_balance("REAL")      # If it's a real account, change the balance to real after reconnecting
        
        # Get the current account balance
        balance = API.get_balance()
        print(f"Current balance: {balance}")  # Print the current account balance
        
        # Get information about market opening times for all assets
        open_times = API.get_all_open_time()
        
        # Loop through the list of opening times to find the first open asset
        symbol = None
        for asset in open_times["turbo"]:
            if open_times["turbo"][asset]["open"]:
                symbol = asset   # Find the first open asset
                break
        
        if symbol is None:
            print("No assets are currently open")
            time.sleep(60)      # If no assets are open, sleep for 60 seconds and continue the loop
            continue
        
        print(f"Trading {symbol}")  # Print the name of the asset to be traded
        
        # Get the RSI indicator value for the last 14 candles
        candles = API.get_candles(symbol, 60, 111, time.time())
        close_prices = [candle["close"] for candle in candles]
        close_prices = np.array(close_prices)  # Convert list of close prices to a NumPy array
        rsi = talib.RSI(close_prices)         # Calculate the RSI indicator

        print(f"Current RSI: {rsi[-1]}")    # Print the current RSI value
        
        # If the RSI is below 30 and the account balance is sufficient, place a call option
        if rsi[-1] < 36 and balance >= amount:
            buy_option = API.buy(1, symbol, 'CALL', amount)  # Place a call option
            print("Call option placed")
            print(API.check_win(buy_option[1]))  # Check if the option is a win
            print(API.check_win(id))  # (Note: 'id' variable is not defined)

        # If the RSI is above 70 and the account balance is sufficient, place a put option
        elif rsi[-1] > 59.8 and balance >= amount:
            buy_option = API.buy(1, symbol, 'PUT', amount)  # Place a put option
            print("Put option placed")
            print(API.check_win(buy_option[1]))  # Check if the option is a win
            print(API.check_win(id))  # (Note: 'id' variable is not defined)

        # Wait for 1 minute before checking again
        time.sleep(60)  # Sleep for 60 seconds before the next iteration
    except (requests.exceptions.HTTPError, ConnectionError, TimeoutError):
        print("Error: Connection lost, attempting to reconnect...")
        time.sleep(5)   # If there's an error, wait for 5 seconds and then continue the loop
        continue
