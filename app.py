from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "The Lord is my Shephered I shall learn flask today"


if __name__ == "__main__":
    app.run(debug=True)
