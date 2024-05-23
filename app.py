from flask import Flask, jsonify
from flask_cors import CORS
import json
from datetime import datetime, timedelta
import pyotp
import time
from SmartApi import SmartConnect
from apscheduler.schedulers.background import BackgroundScheduler

# Initialize the Flask application
app = Flask(__name__)

# Configure CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})  # This enables CORS for all origins for any routes that begin with "/api/"

# Define a route to provide stock data, note the route begins with '/api/' to match the CORS configuration
@app.route('/api/stocks/<type>')
def stocks(type):
    try:
        with open('stock_results.json', 'r') as file:
            data = json.load(file)
        return jsonify(data.get(type, []))  # Return an empty list if type is not found
    except Exception as e:
        return jsonify({'error': str(e)}), 404

def generate_session():
    try:
        uri = 'otpauth://totp/D53948301?secret=DSORJPIYLZN4K4ZHRBJMHCJ3VU&issuer=angelone.in&algorithm=SHA1&digits=6&period=30'
        totp = pyotp.parse_uri(uri)
        token = totp.now()
        print(f"Generated TOTP: {token}")

        obj = SmartConnect(api_key="T1vTIXmj")
        data = obj.generateSession("D53948301", "2211", token)
        obj.setRefreshToken(data['data']['refreshToken'])
        return obj
    except Exception as e:
        print(f"Failed to generate session: {str(e)}")
        return None

def read_stock_file(file_path):
    try:
        with open(file_path, 'r') as file:
            stocks = json.load(file)
        return stocks
    except Exception as e:
        print(f"Failed to read stock file: {str(e)}")
        return []

def scan(symbol_token, obj):
    i = 2  # Start checking from two days ago
    while True:  # Use a true loop to continuously check until break
        today = datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        try:
            historicParam = {
                "exchange": "NSE",
                "symboltoken": symbol_token,
                "interval": "ONE_DAY",
                "fromdate": f"{yesterday} 09:15",
                "todate": f"{today} 09:15"
            }
            response = obj.getCandleData(historicParam)
            # Check if the response data has exactly two entries, if so, return the response
            if len(response["data"]) == 2:
                time.sleep(3)
                return response
            # Increment i if the data length is not 2, to check the next previous day
            i += 1

        except Exception as e:
            print(f"Failed to fetch data for {symbol_token}: {str(e)}")
            return None

def run():
    obj = generate_session()
    if obj:
        file_path = "fno_200_stocks.json"
        stocks = read_stock_file(file_path)
        gap_down_stocks = []
        gap_up_stocks = []
        
        for stock in stocks:
            stock_data = scan(stock['token'], obj)
            if stock_data and "data" in stock_data and len(stock_data["data"]) > 1:
                previous_day = stock_data["data"][0]
                today = stock_data["data"][1]
                # Check for gap down condition
                if previous_day[3] > today[2]:
                    gap_down_stocks.append(stock["symbol"])
                # Check for gap up condition
                if previous_day[2] < today[3]:
                    gap_up_stocks.append(stock["symbol"])

            print(stock["name"])
            time.sleep(3)
        # Save results to JSON file
        with open('stock_results.json', 'w') as file:
                json.dump({'gap_up': gap_up_stocks, 'gap_down': gap_down_stocks}, file)
        print("Results saved.")
    else:
        print("No stocks data available.")

# Schedule the run function to run once a day at 4 PM
scheduler = BackgroundScheduler()
scheduler.add_job(run, 'cron', hour=22, minute=23)
scheduler.start()

# if __name__ == '__main__':
#     app.run(debug=True)
