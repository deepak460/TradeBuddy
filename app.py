from flask import Flask, jsonify, render_template
from flask_cors import CORS
import json

# Initialize the Flask application
app = Flask(__name__)

# Configure CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})  # This enables CORS for all origins for any routes that begin with "/api/"

# Define a basic route to serve the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to provide stock data, note the route begins with '/api/' to match the CORS configuration
@app.route('/api/stocks/<type>')
def stocks(type):
    try:
        with open('stock_results.json', 'r') as file:
            data = json.load(file)
        return jsonify(data.get(type, []))  # Return an empty list if type is not found
    except Exception as e:
        return jsonify({'error': str(e)}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)