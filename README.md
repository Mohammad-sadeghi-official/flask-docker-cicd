
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

## 🏗️ Architecture

```
Client → Nginx (port 80) → Flask (port 5000)
                              ↓
                         Prometheus Metrics
```

---

## 🛠️ Tech Stack

- **Backend:** Flask + Prometheus Client
- **Proxy:** Nginx
- **Containerization:** Docker + Docker Compose
- **CI/CD:** GitHub Actions
- **Registry:** GitHub Container Registry (GHCR)
- **Monitoring:** Prometheus

---

## 📦 Project Structure

```
flask-docker-cicd/
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
└── docker-compose.yml
```

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Mohammad-sadeghi-official/flask-docker-cicd.git
cd flask-docker-cicd
```

### 2. Start the services
```bash
docker compose up -d --build
```

### 3. Access the application
- Application: [http://localhost](http://localhost)
- Health Check: [http://localhost/health](http://localhost/health)
- Metrics: [http://localhost/metrics](http://localhost/metrics)

---

## 🔄 CI/CD Pipeline

On every push to `main`:

1. Checkout the code
2. Login to GitHub Container Registry
3. Build the Docker image
4. Push the image to `ghcr.io/mohammad-sadeghi-official/flask-docker-cicd`

---

## 📊 Metrics Exposed

- `http_requests_total`
- `http_request_duration_seconds`
- `active_requests`

---

## 📌 Future Improvements

- [ ] Add Grafana dashboard
- [ ] Implement proper deployment workflow
- [ ] Add unit tests
- [ ] Support multi-stage Docker build
- [ ] Add HTTPS with Let's Encrypt

---

## 👤 Author

**Mohammad Sadeghi**  
Junior DevOps Engineer  

[LinkedIn](https://www.linkedin.com/in/mohammad-sadeghi1998)
```
