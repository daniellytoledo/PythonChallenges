from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello there! I happy you're here to see how I'm doing with my projects.</p>"
