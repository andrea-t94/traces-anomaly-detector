from flask import Flask, render_template, request, jsonify
from prometheus_client import Counter, generate_latest
from simulation import SimulationManager
from prometheus_flask_exporter import PrometheusMetrics
import threading


app = Flask(__name__)
simulation_manager = SimulationManager()
# Enable Prometheus metrics
metrics = PrometheusMetrics(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trigger_read_spike', methods=['POST'])
def trigger_read_spike():
    duration = int(request.json.get('duration', 10))
    simulation_manager.trigger_read_spike(duration)
    return jsonify({"message": "Read spike triggered", "duration": duration})

@app.route('/trigger_write_spike', methods=['POST'])
def trigger_write_spike():
    duration = int(request.json.get('duration', 10))
    simulation_manager.trigger_write_spike(duration)
    return jsonify({"message": "Write spike triggered", "duration": duration})

@app.route('/crash_db', methods=['POST'])
def crash_db():
    simulation_manager.crash_db()
    return jsonify({"message": "Database crashed"})

@app.route('/restore_db', methods=['POST'])
def restore_db():
    simulation_manager.restore_db()
    return jsonify({"message": "Database restored"})

if __name__ == '__main__':
    threading.Thread(target=simulation_manager.run_simulations).start()
    app.run(host='0.0.0.0', port=5000)
