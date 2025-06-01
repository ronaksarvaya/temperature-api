import os
from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/temperature-data', methods=['GET'])
def get_temperature_data():
    rand_temps = np.random.randint(26, 42, size=365)
    months = [
        ("January", 31), ("February", 28), ("March", 31),
        ("April", 30), ("May", 31), ("June", 30),
        ("July", 31), ("August", 31), ("September", 30),
        ("October", 31), ("November", 30), ("December", 31)
    ]

    data = {}
    day_index = 0

    for month_name, days_in_month in months:
        month_data = {}
        for day in range(1, days_in_month + 1):
            celsius = int(rand_temps[day_index])
            fahrenheit = round((celsius * 9 / 5) + 32, 1)
            month_data[str(day)] = {"celsius": celsius, "fahrenheit": fahrenheit}
            day_index += 1
        data[month_name] = month_data

    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port)
