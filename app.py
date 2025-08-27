from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello PSU Students 6510110218 from Jenkins!"


def test_app():
    assert 1 + 1 == 2


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
