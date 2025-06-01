from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
import os

app = Flask(__name__)
CORS(app)

@app.route('/temperature-data')
def temperature_data():
    # Generate random temperature data for 365 days
    temps = np.random.randint(26, 42, 365).tolist()

    # Number of days in each month (non-leap year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    result = {}
    index = 0
    for i, days in enumerate(month_days):
        result[month_names[i]] = temps[index: index + days]
        index += days

    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
