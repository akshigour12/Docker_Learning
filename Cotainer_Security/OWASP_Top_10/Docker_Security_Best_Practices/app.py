import os
import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Docker Security Best Practices Demo",
        "status": "Running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/env")
def env():
    return jsonify({
        "DB_USERNAME": os.getenv("DB_USERNAME", "Not Set"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD", "Not Set")
    })

if __name__ == "__main__":

    print("=" * 50)
    print("Docker Security Best Practices Demo")
    print("=" * 50)

    print(f"Running as User : {os.getuid()}")
    print(f"DB_USERNAME     : {os.getenv('DB_USERNAME', 'Not Set')}")
    print(f"DB_PASSWORD     : {os.getenv('DB_PASSWORD', 'Not Set')}")

    print("\nApplication started successfully...\n")

    app.run(host="0.0.0.0", port=5000)
