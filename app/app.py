from flask import Flask, request, render_template, jsonify
import threading
import time
import random
from database import insert_data, reset_database

app = Flask(__name__)
normal_load = True
# Enable Prometheus metrics
metrics = PrometheusMetrics(app)

def simulate_normal_load():
    while True:
        if normal_load:
            insert_data()
        time.sleep(1)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/heavy-load", methods=["POST"])
def heavy_load():
    global normal_load
    normal_load = False
    for _ in range(100):  # Simulate 100 write requests
        insert_data()
    return jsonify({"message": "Heavy load simulated"}), 200

@app.route("/crash-db", methods=["POST"])
def crash_db():
    global normal_load
    normal_load = False
    reset_database()
    return jsonify({"message": "Database crashed"}), 200

@app.route("/restore-normal", methods=["POST"])
def restore_normal():
    global normal_load
    normal_load = True
    return jsonify({"message": "Normal load restored"}), 200

if __name__ == "__main__":
    threading.Thread(target=simulate_normal_load, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
