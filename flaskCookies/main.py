from flask import Flask, make_response, request, render_template


app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    saved_name = request.cookies.get("saved_name")
    return render_template("index.html", saved_name=saved_name)


@app.route("/save_name", methods=["POST"])
def save_name():
    name = request.form['name']
    response = make_response(f"We will now remember your name, {name} !")
    response.set_cookie("saved_name", name)
    return response


@app.route("/delete_cookie")
def delete_cookie():
    response = make_response("We will no longer remember your name !")
    response.set_cookie("saved_name", "", expires=0)
    return response


@app.route("/new_cookie")
def new_cookie():
    response = make_response("Hello World!")
    response.set_cookie("mycookie", "myvalue")
    return response


@app.route("/show_cookie")
def show_cookie():
    cookie_value = request.cookies.get("mycookie")
    return cookie_value


if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=9999)
