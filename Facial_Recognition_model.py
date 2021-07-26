# Imported necessary modules
import cv2
import numpy as np
import os

# Loaded haar cascade classifier
face_classifier = cv2.CascadeClassifier('C:/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')

# Given path/location of the folder where our image samples are stored
data_path = 'C:/Users/edwar/PycharmProjects/Face-Recognition/Face_Samples_Dataset/Face_Samples_Dataset/'

# Created two lists for storing our training data and labels associated with them
training_data, labels = [], []

# Traversing the above directory and finding the region of interest from the faces along with  their labels/ID
for path, subdirname, filenames in os.walk(data_path):
    print('path:',path)
    print('subdirname:',subdirname)
    print('filenames:',filenames)

    for file_name in filenames:
        if file_name.startswith('.'):
            print('Skipping system file')  # skipping the system files
            continue

        f_id = os.path.basename(path)  # fetching the sub directory names
        img_path = os.path.join(path,file_name)  # fetching image path
        print('img_path:',img_path)
        print('f_id:',f_id)

        test_img = cv2.imread(img_path)  # loading/reading each image one by one

        # checking if image is loading properly or not
        if test_img is None:
            print('Image not loaded properly !!!')
            continue

        test_gray = cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
        print('test_gray:',test_gray)

        # getting coordinates of the detected faces
        faces = face_classifier.detectMultiScale(test_gray,scaleFactor=1.3,minNeighbors=5)

        if len(faces) != 1:
            continue  # Since we are assuming only single person images are being fed to classifier

        for (x,y,w,h) in faces:
            roi_gray = test_gray[y:y+h,x:x+w]  # cropping region of interest i.e. face area

        roi_gray = cv2.resize(roi_gray,(500,500))  # Resizing the cropped region

        # Preparing data for training
        training_data.append(roi_gray)  # Appending the face portions/region of interest and creating the training data
        labels.append(int(f_id))  # Appending the labels associated with the faces detected

# creating model using LBPH face recognizer
model = cv2.face.LBPHFaceRecognizer_create()

# Training the data
model.train(np.asarray(training_data),np.asarray(labels))

# Saving the trained model
model.save('Training_data.yml')

print('Model training complete !!!')








