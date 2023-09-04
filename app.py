from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("templates\login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username.capitalize() and password.isalnum():
        return redirect("/login-success")
    else:
        return redirect("/")

@app.route("/login-success")
def login_success():
    return render_template("templates\login-success.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)