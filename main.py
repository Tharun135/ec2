# main.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world! Your Flask app is running on EC2 🚀"

if __name__ == "__main__":
    # Run on all interfaces so it’s accessible via public IP
    app.run(host="0.0.0.0", port=5000, debug=True)
