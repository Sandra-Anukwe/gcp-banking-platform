# GCP Banking Platform 

A simulated online banking platform built on **Google Cloud** to demonstrate secure, scalable architecture and real-world DevOps practices.

##  Overview
This project showcases:
- Cloud-native **API** (Python/Flask) packaged with Docker
- Deployment to **Cloud Run** (serverless) with zero-maintenance scaling
- **Cloud SQL (PostgreSQL)** for relational data
- **Cloud Storage** for static assets and exports
- **IAM-first security** with least-privilege roles
- Basic **observability** with Cloud Logging/Monitoring (roadmap)

> Designed as a portfolio-grade project for recruiters and MSc reviewers.

---

## Architecture (MVP)
- **Client:** (future) Web UI or Postman
- **Service:** Flask API container on **Cloud Run**
- **Data:** **Cloud SQL (PostgreSQL)** via SQL connector
- **Storage:** **Cloud Storage** for receipts/exports
- **Networking/Sec:** VPC, IAM, service accounts, secrets

See: [`docs/architecture.md`](docs/architecture.md)

---

## Quickstart (Local)
**Requirements:** Python 3.10+, Git, Docker (optional)

```bash
# 1) Create & activate a virtualenv
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run the API
export FLASK_APP=main.py  # (setenv for Windows: set FLASK_APP=main.py)
flask run --port 8080

# Visit http://127.0.0.1:8080
```

**Docker (optional):**
```bash
docker build -t gcp-banking-platform:dev .
docker run -p 8080:8080 gcp-banking-platform:dev
```

---

## Deploy to Cloud Run (sample flow)
> Ensure you have gcloud CLI installed and are logged in to the correct project.

```bash
# 1) Enable services (one-time)
gcloud services enable run.googleapis.com cloudbuild.googleapis.com sqladmin.googleapis.com

# 2) Build & push container via Cloud Build
gcloud builds submit --tag gcr.io/$(gcloud config get-value project)/gcp-banking-platform

# 3) Deploy to Cloud Run
gcloud run deploy gcp-banking-platform \
  --image gcr.io/$(gcloud config get-value project)/gcp-banking-platform \
  --platform managed \
  --region europe-west2 \
  --allow-unauthenticated
```

> Later, add a Cloud SQL connection and secrets for DB credentials (see roadmap).

---

## Repo Structure
```
gcp-banking-platform/
├─ README.md
├─ main.py
├─ requirements.txt
├─ Dockerfile
├─ .gitignore
├─ .env.example
├─ docs/
│  ├─ architecture.md
│  └─ deployment-notes.md
├─ scripts/
│  └─ seed_db.sql
├─ images/
│  └─ .gitkeep
└─ .github/workflows/
   └─ ci.yml
```

---

## Roadmap
- [ ] Add `/accounts`, `/transactions` endpoints
- [ ] Integrate **Cloud SQL** with secure connector
- [ ] Configure secrets (DB URL) via **Secret Manager**
- [ ] Add **unit tests** and CI with pytest
- [ ] Basic Web UI (optional) or Postman collection
- [ ] Monitoring dashboards (Cloud Monitoring)

---

##  Security Notes
- Use **least privilege** IAM for the Cloud Run service account
- Never commit secrets – use **Secret Manager** and `.env` locally
- Add **VPC egress** and private IP for Cloud SQL in production

---

✅ Auto-deploy test via Cloud Build – triggered by Sandra Anukwe

##  License
MIT © 2025 Sandra Anukwe
- Cloud Build Trigger test Sat Oct 18 02:50:09 PM UTC 2025
- Cloud Build Trigger test Sat Oct 18 02:51:56 PM UTC 2025
- trigger OK Sat Oct 18 03:21:39 PM UTC 2025
- kick build Thu Oct 23 02:09:41 PM UTC 2025
