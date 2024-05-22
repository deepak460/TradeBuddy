import numpy as np
import pandas as pd
import pyotp
from datetime import datetime, timedelta
import json
import time
from SmartApi import SmartConnect

def generate_session():
    try:
        totp = pyotp.TOTP('DSORJPIYLZN4K4ZHRBJMHCJ3VU')
        token = totp.now()
        print(f"Generated TOTP: {token}")
    
        # Initialize SmartConnect with your API key
        obj = SmartConnect(api_key="T1vTIXmj")
        data = obj.generateSession("D53948301", "2211", token)
        refreshToken = data['data']['refreshToken']
        obj.setRefreshToken(refreshToken)  # Corrected method name
        return obj
    except Exception as e:
        print(f"Failed to generate session: {str(e)}")
        return None

def read_stock_file(file_path):
    try:
        with open(file_path, 'r') as file:
            stocks = json.load(file)
            print("stocks = ", stocks)
        return stocks
    except Exception as e:
        print(f"Failed to read stock file: {str(e)}")
        return []

def fetch_stock_data(symbol_token, obj):
    today = datetime.now()
    start_date = today - timedelta(days=30)
    historicParam = {
        "exchange": "NSE",
        "symboltoken": symbol_token,
        "interval": "ONE_DAY",
        "fromdate": start_date.strftime("%Y-%m-%d 09:15"),
        "todate": today.strftime("%Y-%m-%d 15:30")
    }
    try:
        response = obj.getCandleData(historicParam)
        print(response)
        if 'data' in response and response['data']:
            data = pd.DataFrame(response['data'], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            data['close'] = pd.to_numeric(data['close'])
            return data
        else:
            raise ValueError("No data returned from API")
    except Exception as e:
        print(f"Failed to fetch data for {symbol_token}: {str(e)}")
        return pd.DataFrame()

def calculate_moving_average(data, window=30):
    if not data.empty:
        ma = data['close'].rolling(window=window).mean()
        if ma.iloc[-1] > ma.iloc[-2]:  # Check if the MA is rising
            return ma.iloc[-1]
    return None

# def scan_stocks(stock_list, obj):
#     results = {}
#     for stock in stock_list:
#         data = fetch_stock_data(stock['token'], obj)
#         print(stock['symbol'])
#         if not data.empty:
#             ma30 = calculate_moving_average(data)
#             current_price = data['close'].iloc[-1]
#             if ma30 and np.isclose(current_price, ma30, atol=ma30*0.01):
#                 results[stock['symbol']] = (current_price, ma30)
#     return results

if __name__ == "__main__":
    obj = generate_session()
    if obj:
        file_path = 'fno_200_stocks.json'
        stocks = read_stock_file(file_path)
        # results = scan_stocks(stocks, obj)
        # print("Stocks taking support at 30-day MA:", results)
        print (" test")
