from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello, Paul</h1>"


@app.route('/hello', methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return "You made GET request"
    elif request.method == 'POST':
        return "You made POST request"


@app.route('/hello2', methods=['GET'])
def hello2():
    response = make_response()
    response.status_code = 500
    response.headers['content-type'] = 'application/octet-stream'
    return response


@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"


@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f'{greeting} {name}'
    else:
        return 'Parameters not available'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)