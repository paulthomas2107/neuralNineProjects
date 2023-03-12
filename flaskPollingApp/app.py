import os.path

import pandas as pd
from flask import Flask, render_template, redirect, request, url_for, make_response

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return "Hello, Paul"


if __name__ == "__main__":
    app.run(host="localhost", debug=True)