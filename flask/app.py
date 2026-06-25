from flask import Flask, request
from prometheus_client import (
    Counter,
    Histogram,
    Gauge,
    generate_latest,
    CONTENT_TYPE_LATEST
)

import time

app = Flask(__name__)


from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)


# ==================================
# Metrics
# ==================================

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP Request Duration",
    ["method", "endpoint"]
)

ACTIVE_REQUESTS = Gauge(
    "active_requests",
    "Number of active requests"
)

# ==================================
# Hooks
# ==================================

@app.before_request
def before_request():
    request.start_time = time.time()
    ACTIVE_REQUESTS.inc()


@app.after_request
def after_request(response):

    duration = time.time() - request.start_time

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        status=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.path
    ).observe(duration)

    ACTIVE_REQUESTS.dec()

    return response


# ==================================
# Routes
# ==================================

@app.route("/")
def hello_world():
    return "<p>Hello from Dockerized Flask!</p>"


@app.route("/health")
def health():
    return {"status": "ok"}


# ==================================
# Prometheus Metrics Endpoint
# ==================================

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
