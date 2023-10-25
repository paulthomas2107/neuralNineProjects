import math
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    calculation = math.pi * 2
    return render_template('index.html', some_text="hello, paul !", some_number=2.65, calc_001=calculation)


@app.template_filter("reverse_string")
def reverse_string_filer(s):
    return s[::-1]


@app.template_filter("alternate")
def alternate_filter(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])


@app.template_filter("repeat")
def repeat(s, times=2):
    return s * times


if __name__ == "__main__":
    app.run(debug=True)