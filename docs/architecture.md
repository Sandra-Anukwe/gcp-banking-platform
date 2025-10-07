# Architecture

## MVP Diagram (Conceptual)
- Client → Cloud Run (Flask API)
- Cloud Run → Cloud SQL (PostgreSQL) via SQL Connector
- Cloud Run → Cloud Storage for receipts/exports
- IAM controls for all resources; no long-lived user keys

## Notes
- Start with unauthenticated public endpoints for demo; later add auth (OAuth 2.0 / Firebase Auth).
- Use service accounts for Cloud Run with least-privilege role bindings.
- Prefer private IP for Cloud SQL in production to limit exposure.
