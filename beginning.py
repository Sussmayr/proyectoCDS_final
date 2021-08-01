from types import MethodType
from flask import Flask, redirect, url_for, render_template, request, flash
from flask.globals import session
from flask.wrappers import Request
from werkzeug import secure_filename

import os

app = Flask (__name__)

app.secret_key = "hello" #the encription password


database={"Edward":"Pass123","ingrid":"Pass123"}

@app.route('/')
def home():
    return render_template("index.html")

###

@app.route('/success/<name>/<passwrd>')
def Success(name,passwrd):
    if name in database.keys():
        if passwrd==database[name]:
            return "<h1>Welcome!!!</h1>"
        else:
            return "<h1>Invalid Username or password</h1>"
    else:
        return "<h1>Username doesn't exists.</h1>"

@app.route('/fetch_data',methods=['POST','GET'])
def FetchData():
    if request.method=="POST":
        user=request.form['nm']
        password=request.form['pw']
        return redirect(url_for('Success',name=user,passwrd=password))
    else:
        user = request.args.get('nm')
        password = request.args.get('pw')
        return redirect(url_for('Success', name=user,passwrd=password))

###

# Carpeta de subida
app.config['UPLOAD_FOLDER'] = 'C:/Users/edwar/OneDrive/Documentos/proyecto CDS_final/proyectoCDS_final/Face_Samples_Dataset/imagenes'

@app.route("/")
def upload_file():
    # renderiamos la plantilla "formulario.html"
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "Archivos"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Retornamos una respuesta satisfactoria
        #return "<h1>Archivo subido exitosamente</h1>"
        fullpath = 'C:/Users/edwar/OneDrive/Documentos/proyecto CDS_final/proyectoCDS_final/Face_Samples_Dataset/imagenes/'+filename
        #return fullpath
        #return "<h1>Archivo subido exitosamente</h1>" + fullpath + '<h1><a href="/"><button>Regresar</button></a></h1>'
        return render_template("upload.html") + fullpath
###

@app.route('/scan/')
def scan():
  exec(open('Image_scan_recognition.py').read())
  return render_template("index.html")


# login validations
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

        return render_template("user.html", user=user, email=email)
    else:
        flash("No has iniciado session")
        return redirect(url_for("login"))

# salir de la session
@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash("la Session ha sido cerrada!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


#abrir camara
@app.route('/webcam')
def cam():
    return render_template("webcam.html")

if __name__ == "__main__":
    app.run(debug=True)