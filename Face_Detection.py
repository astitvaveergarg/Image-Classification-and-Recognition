import cv2
import numpy as np

face = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
proflie = cv2.CascadeClassifier('./Haarcascade Files Face Detection\haarcascade_profileface.xml')
def face_recognition(path):
        image1=cv2.imread(path)
        image = image1.copy()
        width = int(image.shape[1]/10)
        height = int(image.shape[0]/10)
        # image1 = cv2.resize(image, (1000-height,1000-width))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face.detectMultiScale(gray, 1.1, 1)
        # profile_faces = proflie.detectMultiScale(gray,1.1,1)

        for (x,y,w,h) in faces:
                predicted_face = cv2.rectangle(image, (x,y) , (x+w,y+h) , (225,0,0) , 1 )

        # for (x,y,w,h) in profile_faces:
        #         predicted_face = cv2.rectangle(image, (x,y) , (x+w,y+h) , (0,0,225) , 1 )
        
        return faces,image1