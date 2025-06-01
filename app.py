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

    return jsonify(result)
