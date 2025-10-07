from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def root():
    return jsonify({
        "service": "Banking Platform API",
        "status": "ok",
        "message": "Hello from Cloud Run-ready Flask app!"
    })

if __name__ == '__main__':
    # For local dev; Cloud Run uses gunicorn (see Dockerfile)
    app.run(host='0.0.0.0', port=8080, debug=True)
