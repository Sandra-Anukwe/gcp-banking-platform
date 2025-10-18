from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory demo data
ACCOUNTS = [
    {"id": 1, "name": "Main Current", "type": "current", "balance": 1200.50, "currency": "GBP"},
    {"id": 2, "name": "Savings", "type": "savings", "balance": 3000.00, "currency": "GBP"},
]
TRANSACTIONS = [
    {"id": 1, "account_id": 1, "amount": -25.40, "currency": "GBP", "desc": "Lunch"},
    {"id": 2, "account_id": 2, "amount": 200.00, "currency": "GBP", "desc": "Interest"},
]

@app.get("/")
def root():
    return jsonify({"service": "Banking Platform API", "status": "ok"})

@app.get("/accounts")
def list_accounts():
    return jsonify({"accounts": ACCOUNTS})

@app.post("/accounts")
def create_account():
    payload = request.get_json(force=True)
    new_id = max(a["id"] for a in ACCOUNTS) + 1 if ACCOUNTS else 1
    account = {
        "id": new_id,
        "name": payload.get("name", f"Account {new_id}"),
        "type": payload.get("type", "current"),
        "balance": float(payload.get("balance", 0.0)),
        "currency": payload.get("currency", "GBP"),
    }
    ACCOUNTS.append(account)
    return jsonify(account), 201

@app.get("/transactions")
def list_transactions():
    return jsonify({"transactions": TRANSACTIONS})

@app.post("/transactions")
def create_transaction():
    payload = request.get_json(force=True)
    new_id = max(t["id"] for t in TRANSACTIONS) + 1 if TRANSACTIONS else 1
    tx = {
        "id": new_id,
        "account_id": int(payload["account_id"]),
        "amount": float(payload["amount"]),
        "currency": payload.get("currency", "GBP"),
        "desc": payload.get("desc", ""),
    }
    TRANSACTIONS.append(tx)
    # Optional: update account balance
    for a in ACCOUNTS:
        if a["id"] == tx["account_id"]:
            a["balance"] += tx["amount"]
            break
    return jsonify(tx), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
