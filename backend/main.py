from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, {os.getenv('NAME')}!</p>"

@app.route("/ping")
def ping():
    return "pong"

if __name__ == '__main__':
    app.run(debug=True, use_debugger=True, use_reloader=False, port=8080)