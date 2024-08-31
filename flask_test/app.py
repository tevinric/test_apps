# Save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is my Flask app!"

if __name__ == "__main__":
    app.run()
