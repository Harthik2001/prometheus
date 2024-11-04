from flask import Flask, request, jsonify, render_template
from prometheus_client import Counter, Gauge, generate_latest, CollectorRegistry
import psutil

app = Flask(__name__)



# Prometheus metrics
registry = CollectorRegistry()
http_request_counter = Counter('http_request_count', 'Total number of HTTP requests', registry=registry)
memory_usage_gauge = Gauge('memory_usage_bytes', 'Memory usage in bytes', registry=registry)
cpu_usage_gauge = Gauge('cpu_usage_percentage', 'CPU usage percentage', registry=registry)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    http_request_counter.inc()  # Increment counter
    data = request.json
    value = data['value']
    from_unit = data['from']
    to_unit = data['to']
    
    # Collect metrics
    memory_usage_gauge.set(psutil.virtual_memory().used)
    cpu_usage_gauge.set(psutil.cpu_percent())

    conversions = {
        ('km', 'miles'): value * 0.621371,
        ('miles', 'km'): value / 0.621371,
        ('kg', 'pounds'): value * 2.20462,
        ('pounds', 'kg'): value / 2.20462,
        ('celsius', 'fahrenheit'): (value * 9 / 5) + 32,
        ('fahrenheit', 'celsius'): (value - 32) * 5 / 9,
    }

    result = conversions.get((from_unit, to_unit))
    if result is not None:
        return jsonify({'result': result})
    else:
        return jsonify({'message': 'Invalid conversion'}), 400

@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(registry), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)