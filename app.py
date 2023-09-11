from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "anything"

app.run(debug=True, port=5001)

