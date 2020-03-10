import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hi there!"

app.run(host="0.0.0.0", port=7500)