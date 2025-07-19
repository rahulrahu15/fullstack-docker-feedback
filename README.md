# 📝 Full Stack Feedback App (Dockerized + CI/CD)

A fully containerized full-stack feedback application built with Flask (Python) and a frontend (e.g., React or HTML/CSS), deployed on AWS EC2 with automated CI/CD using GitHub Actions.



## 📦 Tech Stack

| Layer     | Tech Used                  |
|----------|----------------------------|
| Frontend | HTML/CSS/JavaScript or React |
| Backend  | Flask (Python)             |
| Database | (Optional: SQLite / MongoDB)|
| DevOps   | Docker, Docker Compose     |
| CI/CD    | GitHub Actions             |
| Hosting  | AWS EC2 (Ubuntu)           |
| DNS      | DuckDNS (Free Dynamic DNS) |

---

## 🚀 Features

- 📩 Submit feedback via a simple UI
- ⚙️ Backend API to receive and store feedback
- 🐳 Fully Dockerized setup using `docker-compose`
- 🔄 CI/CD pipeline with GitHub Actions
- ☁️ Deployed on AWS EC2
- 🆓 Free domain via DuckDNS

---

## 📁 Project Structure

fullstack-docker-feedback/
├── backend/
│ └── app.py
├── frontend/
│ └── index.html
├── docker-compose.yml
├── Dockerfile (backend)
├── .github/workflows/ci-cd.yml
└── README.md


---

## ⚙️ CI/CD Pipeline Overview

1. **Trigger:** On `git push` to `main` branch
2. **GitHub Action:** Runs workflow in `.github/workflows/ci-cd.yml`
3. **SSH into EC2:** Uses GitHub Secrets for private key & host
4. **Remote Deployment:**
   - Pulls latest code
   - Rebuilds Docker containers
   - Restarts app with `docker-compose`

---

## 🔐 GitHub Secrets

| Name           | Description                      |
|----------------|----------------------------------|
| `EC2_HOST`     | EC2 public IP or DNS name        |
| `EC2_SSH_KEY`  | Your EC2 private key (OpenSSH format) |

---

## 🛠️ Setup Instructions

### 1. 🧪 Local Development

```bash
docker-compose up --build
docker-compose -d
docker-compose down


