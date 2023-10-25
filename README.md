# IQ Option Trading Bot

## Quick Description
This Python script is designed to automate trading on the IQ Option platform using technical analysis indicators. It utilizes the IQ Option API, Numpy, and TA-Lib for trading based on the Relative Strength Index (RSI) indicator. You can configure the script to place CALL or PUT options when certain RSI conditions are met.

## Installation
To use this script, follow these steps to set up the required dependencies:

1. Clone the repository to your local machine:
```bash
   git clone https://github.com/yourusername/iq-option-trading-bot.git
```
```bash
   cd iq-option-trading-bot
```

2-Create a virtual environment (optional but recommended) and activate it:
```bash
python -m venv venv
```
```bash
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3-Install the required packages from the requirements.txt file:
```bash
pip install -r requirements.txt
```

Usage
To use the script to automate trading on IQ Option, follow these instructions:

Replace the placeholders in the script with your IQ Option email and password.

Set the amount variable to the amount you want to trade.

Specify whether you want to use a demo (virtual) or real account by setting the demo_account variable to True for a demo account or False for a real account.

Run the script:
```bash
python IQ option Trading.py
```
The script will continuously monitor the RSI indicator of the selected asset and place CALL or PUT options based on your configured RSI conditions. It will automatically handle reconnections and account switching.

Note: Ensure that you have an IQ Option account, and use this script responsibly. Trading involves risk, and you should understand the risks associated with trading before using this bot, and I am not responsible for any loss.

Please make sure to review and understand the code and trading strategies before using the script in a live environment.

## Support This simple script to continue updating 
If you find this project helpful and would like to support its development, you can make a donation through the following platforms:

Donate - [PayPal](https://www.paypal.com/paypalme/fadykelliny)
