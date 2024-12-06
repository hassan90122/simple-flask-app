from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # Automatically adds a /metrics endpoint

@app.route('/')
def hello():
    return "Hello, Giza Systems Headways!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

