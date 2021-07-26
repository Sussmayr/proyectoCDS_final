from types import MethodType
from flask import Flask, redirect, url_for, render_template, request, flash
from flask.globals import session
from flask.wrappers import Request

app = Flask (__name__)
app.secret_key = "hello" #the encription password

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        #user = request.form["pwd"]
        session["user"] = user
        flash("Accediste correctamente!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("ya has accedido a la session")
            return redirect(url_for("user"))
        
        return render_template("login.html")

#the sesion is encrypted
@app.route("/user", methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("correo a sido guardado!")
        else:
            if "email" in session:
                email =session["email"]

        return render_template("user.html", email=email)
    else:
        flash("No has iniciado session")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash("la Session ha sido cerrada!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)