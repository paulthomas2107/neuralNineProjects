from flask import Flask, request

app = Flask(__name__)


@app.route("/webhoolkcallback", methods=["POST"])
def hook():
    print(request.data)
    return "Hello, Paul !"


if __name__ == "__main__":
    app.run()