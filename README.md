# Flask + Docker + CI/CD

A complete practice project for containerizing a Flask application with **Nginx**, **Prometheus metrics**, and a full **GitHub Actions CI/CD pipeline**.

---

## 🚀 Features

- Flask application with health check endpoint
- Prometheus metrics (request count, latency, active requests)
- Nginx as reverse proxy
- Docker & Docker Compose setup
- Healthcheck for the Flask service
- GitHub Actions CI: Build & push Docker image to **GitHub Container Registry (GHCR)**
- Separate monitoring stack (Prometheus)

---

## 🏗️ ArchitectureClient → Nginx (port 80) → Flask (port 5000)
↓
Prometheus Metricstext---

## 🛠️ Tech Stack

- **Backend:** Flask + Prometheus Client
- **Proxy:** Nginx
- **Containerization:** Docker + Docker Compose
- **CI/CD:** GitHub Actions
- **Registry:** GitHub Container Registry (GHCR)
- **Monitoring:** Prometheus , Grafana

---

## 📦 Project Structureflask-docker-cicd/
├── flask/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── nginx/
│   └── default.conf
├── monitoring/
│   └── ...
├── .github/workflows/
│   ├── ci.yml
│   ├── deploy.yml
│   └── release.yml
└── docker-compose.ymltext---

## ▶️ How to Run

### 1. Clone the repository
git clone https://github.com/Mohammad-sadeghi-official/flask-docker-cicd.git
cd flask-docker-cicd2. Start the servicesBashdocker compose up -d --build3. Access the application
Application: http://localhost
Health Check: http://localhost/health
Metrics: http://localhost/metrics

🔄 CI/CD PipelineOn every push to main:
Checkout the code
Login to GitHub Container Registry
Build the Docker image
Push the image to ghcr.io/mohammad-sadeghi-official/flask-docker-cicd

📊 Metrics Exposed
http_requests_total
http_request_duration_seconds
active_requests

📌 Future Improvements
 Add Grafana dashboard
 Implement proper deployment workflow
 Add unit tests
 
 👤 Author : Mohammad Sadeghi
Junior DevOps Engineer
 Support multi-stage Docker build
 Add HTTPS with Let's Encrypt
 
