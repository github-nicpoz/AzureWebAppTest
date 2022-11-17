from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>Hello Best Bike App from GitHub - Version 2!</h1></body></html>\n"
