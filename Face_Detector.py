from flask import Flask, redirect, url_for, render_template, request, flash

# Importing necessary module
import cv2

# Loading training data
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('C:/Users/edwar/OneDrive/Documentos/proyecto CDS_final/proyectoCDS_final/Training_data.yml')

# some initializations
x,y,w,h = 0,0,0,0
l = ''

# Function for detecting the faces and drawing rectangular frames around faces
def face_detector(img):

    global x,y,w,h
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting colored image to grayscale

    # Loading haar cascade classifier
    face_classifier = cv2.CascadeClassifier('C:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')

    # getting coordinates of the detected faces
    faces = face_classifier.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=7)

    if faces == ():
        return img,[]

    # Drawing rectangular frames around detected faces
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h,x:x+w]  # cropping region of interest i.e. face area
        roi = cv2.resize(roi,(500,500))  # Resizing the cropped region

    return img,roi

#creating dictionary containing names for each label
name = {0:'Edward',1:'Ingrid', 2:'Einstein'}

# capturing video capture object
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret,img_frame = cap.read()  # Reading images from web camera

    image,req_face = face_detector(img_frame)  # calling face_detector() method


    try:
        req_face = cv2.cvtColor(req_face, cv2.COLOR_BGR2GRAY)
        label, confidence = face_recognizer.predict(req_face)  # predicting the label of given image
        print('Confidence :',confidence)
        print('Label :',label)

        l = label

        face_label = name[label]  # finding face labels to be displayed on rectangular frames
        #print(face_label)

        #
        if (label == l) and (confidence < 50):
            print('Face Recognized !!!')
            cv2.putText(image, face_label, (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)  # displaying 'Name' of the recognized face
            cv2.imshow('Face Recognizer', image)

        else:
            print('Unknown Face !!!')
            cv2.putText(image, 'Unknown', (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)  # displaying 'Unknown' when unknown face is recognized
            cv2.imshow('Face Recognizer', image)

    except:
        print('Face not found')
        cv2.putText(image, 'X X X ! Face Not Found ! X X X', (50, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)  # displaying 'Face not found' when no face is recognized
        cv2.imshow('Face Recognizer', image)
        pass

    if cv2.waitKey(1)==13:  # Waits indefinitely until enter key is pressed
        break  # stop the program and closing the camera window

cap.release()  # releasing the camera
cv2.destroyAllWindows()
