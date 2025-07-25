from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
import os
from collections import OrderedDict

app = Flask(__name__)
CORS(app)

@app.route('/')
def redirect():
    return "Add /temperature-data in the URL"

@app.route('/temperature-data')
def temperature_data():
    temps = np.random.randint(26, 42, 365).tolist()
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    result = []
    index = 0
    for i, days in enumerate(month_days):
        result.append({
            "month": month_names[i],
            "temps": temps[index: index + days]
        })
        index += days

    ordered_data = OrderedDict()
    for entry in result:
        ordered_data[entry["month"]] = entry["temps"]

    return jsonify({
        "data": ordered_data,
        "order": month_names
    })
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
