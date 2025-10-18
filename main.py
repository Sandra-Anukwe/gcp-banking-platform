# main.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/health")
def health():
    return {"status": "ok"}, 200

@app.get("/")
def home():
    return jsonify(message="Banking API running on Cloud Run"), 200

# example endpoint you can expand later
@app.get("/balance")
def balance():
    # demo response
    account_id = request.args.get("account_id", "demo-123")
    return jsonify(account_id=account_id, balance=1250.40, currency="GBP"), 200

if __name__ == "__main__":
    # for local testing only; Cloud Run will use gunicorn from the Dockerfile
    import os
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
