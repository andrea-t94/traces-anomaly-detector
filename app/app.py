from flask import Flask, jsonify, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
from database import insert_data, read_data

app = Flask(__name__)

# Prometheus metrics exporter setup
metrics = PrometheusMetrics(app)

@app.route('/')
def welcome():
    return render_template('index.html')

# Define a route to fetch data from the MariaDB database
@app.route('/data', methods=['GET'])
def get_data():
    # Check if the 'overload' or 'db_issue' query parameters are set
    overload = request.args.get('overload', 'false').lower() == 'true'
    db_issue = request.args.get('db_issue', 'false').lower() == 'true'

    # Handle overload scenario (50% chance to return 503 Service Unavailable)
    if overload:
        if random.random() < 0.5:  # 50% chance of failure
            return jsonify({"error": "Service Unavailable due to overload"}), 503

    # Handle database issue scenario (always return 500 Internal Server Error)
    if db_issue:
        return jsonify({"error": "Database connection issue"}), 500

    # Normal flow - connecting to the database
    try:
        result = read_data()
        # Convert rows to a dictionary list for JSON response
        data = [{"value": row[0]} for row in rows]
        return jsonify(data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to check if the application is running
@app.route('/health', methods=['GET'])
def health_check():
    return "Healthy", 200

# Run the application on port 5000
if __name__ == '__main__':
    insert_data()
    app.run(host='0.0.0.0', port=5000)
