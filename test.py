from flask import Flask, redirect, url_for, render_template, request
from flask.globals import session
from flask.wrappers import Request

app = Flask (__name__)

@app.route("/")
def home():
    return render_template("index.html")

#pass parameters
@app.route("/<name>")
def home(name):
    return render_template("index.html", content=["Tim", "Ed", "Chris"])

@app.route("/")
def home():
    return "Hello! this is the main page <h1>HELLO<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    #redirect if not admin
    return redirect(url_for("user", name="Admin!!"))

if __name__ == "__main__":
    app.run(debug=True)