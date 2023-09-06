from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('login.html', template_folder='auth')

@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username.capitalize() and password.isalnum():
        return render_template('login-success.html', template_folder='auth')
    else:
        return render_template('login.html', template_folder='auth')

@app.route("/login-success", methods=["GET"])
def login_success():
    return render_template('login-success.html', template_folder='auth')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)