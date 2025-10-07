# Deployment Notes

## Prerequisites
- gcloud CLI installed and authenticated
- A GCP project with billing enabled
- Cloud Run, Cloud Build, Cloud SQL Admin APIs enabled

## Steps (high-level)
1. Build the container with Cloud Build and push to GCR/Artifact Registry
2. Deploy to Cloud Run (region: europe-west2 or your choice)
3. Configure environment variables and secrets
4. (Later) Bind Cloud SQL connection and run DB migrations
