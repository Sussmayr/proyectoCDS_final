from flask import Flask, redirect, url_for, render_template, request, flash

import cv2
import face_recognition

# Cargamos las imagenes con los rostros que queremos identificar:
imagen_paul = face_recognition.load_image_file("C:/Users/edwar/OneDrive/Documentos/proyecto CDS/reconocimiento-facial-CDS/imagenes/paul.jpg")
imagen_einstein = face_recognition.load_image_file("C:/Users/edwar/OneDrive/Documentos/proyecto CDS/reconocimiento-facial-CDS/imagenes/einstein.jpg")
imagen_planck = face_recognition.load_image_file("C:/Users/edwar/OneDrive/Documentos/proyecto CDS/reconocimiento-facial-CDS/imagenes/planck.jpg")
imagen_ingrid = face_recognition.load_image_file("C:/Users/edwar/OneDrive/Documentos/proyecto CDS/reconocimiento-facial-CDS/imagenes/Ingrid.jpg")
imagen_edward = face_recognition.load_image_file("C:/Users/edwar/OneDrive/Documentos/proyecto CDS_final/proyectoCDS_final/Face_Samples_Dataset/0/Edward1.jpg")


# El siguiente paso es extraer los 'encodings' de cada imagen.
# Los encodings son las caracterasticas unicas de cada ropip install cmakestro que permiten diferenciarlo de otros.
einstein_encodings = face_recognition.face_encodings(imagen_einstein)[0]
paul_encodings = face_recognition.face_encodings(imagen_paul)[0]
planck_encodings = face_recognition.face_encodings(imagen_planck)[0]
ingrid_encodings = face_recognition.face_encodings(imagen_ingrid)[0]
edward_encodings = face_recognition.face_encodings(imagen_edward)[0]

# Creamos un array con los encodings y otro con sus respectivos nombres:
encodings_conocidos = [
    einstein_encodings,
    paul_encodings,
    planck_encodings,
    ingrid_encodings,
    edward_encodings
]
nombres_conocidos = [
    "Albert Einstein",
    "Paul Langevin",
    "Max Planck",
    "Ingrid Mejia",
    "Edward Flores"
]

# Cargamos una fuente de texto:
font = cv2.FONT_HERSHEY_COMPLEX

# Cargamos la imagen donde hay que identificar los rostros:
img = face_recognition.load_image_file('C:/Users/edwar/OneDrive/Documentos/proyecto CDS/reconocimiento-facial-CDS/imagenes/IMG_20210604_194122.jpg')
# (Para probar la segunda imagen hay que cambiar el argumento de la funcion por 'imagen_input2.jpg')


# Definir tres arrays, que serviran para guardar los parametros de los rostros que se encuentren en la imagen:
loc_rostros = []  # Localizacion de los rostros en la imagen (contendra las coordenadas de los recuadros que las contienen)
encodings_rostros = []  # Encodings de los rostros
nombres_rostros = []  # Nombre de la persona de cada rostro

# Localizamos cada rostro de la imagen y extraemos sus encodings:
loc_rostros = face_recognition.face_locations(img)
encodings_rostros = face_recognition.face_encodings(img, loc_rostros)

# Recorremos el array de encodings que hemos encontrado:
for encoding in encodings_rostros:

    # Buscamos si hay alguna coincidencia con algun encoding conocido:
    coincidencias = face_recognition.compare_faces(encodings_conocidos, encoding)

    # El array 'coincidencias' es ahora un array de booleanos.
    # Si contiene algun 'True', es que ha habido alguna coincidencia:
    if True in coincidencias:
        # Buscamos el nombre correspondiente en el array de nombres conocidos:
        nombre = nombres_conocidos[coincidencias.index(True)]

    # Si no hay ningun 'True' en el array 'coincidencias', no se ha podido identificar el rostro:
    else:
        nombre = "???"

    # Añadimos el nombre de la persona identificada en el array de nombres:
    nombres_rostros.append(nombre)

# Dibujamos un recuadro rojo alrededor de los rostros desconocidos, y uno verde alrededor de los conocidos:
for (top, right, bottom, left), nombre in zip(loc_rostros, nombres_rostros):

    # Cambiar el color segun el nombre:
    if nombre != "???":
        color = (0, 255, 0)  # Verde
    else:
        color = (0, 0, 255)  # Rojo

    # Dibujar los recuadros alrededor del rostro:
    cv2.rectangle(img, (left, top), (right, bottom), color, 2)
    cv2.rectangle(img, (left, bottom - 20), (right, bottom), color, -1)

    # Escribir el nombre de la persona:
    cv2.putText(img, nombre, (left, bottom - 6), font, 0.6, (0, 0, 0), 1)

# Abrimos una ventana con el resultado:
cv2.imshow('Output', img)
print("\nMostrando resultado. Pulsa cualquier tecla para salir.\n")
cv2.waitKey(0)
cv2.destroyAllWindows()