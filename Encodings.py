import Face_Detection
from imutils import paths
import cv2
import dlib
import face_recognition
import os
import random

def main(image_path):
    imagePaths = list(paths.list_images("./dataset"))
    knownEncodings = []
    knownNames = []
    Results = []

    for imagePaths1 in imagePaths:

        faces,imagemarking = Face_Detection.face_recognition(imagePaths1)
        for (x,y,w,h) in faces:
            train_encodings = face_recognition.face_encodings(imagemarking)
            if train_encodings==None:
                knownEncodings.append(False)
            else:
                knownEncodings.append(train_encodings)
        label = imagePaths1.split(os.path.sep)[-2]     
        knownNames.append(label)

    filename1=str(random.randint(0,100000000000000))
    filename=filename1+'.jpg'

    faces1,image1 = Face_Detection.face_recognition(image_path)
    test_encodings1 = face_recognition.face_encodings(image1)

    for  i in knownEncodings:
        Result=face_recognition.compare_faces(i,test_encodings1[0])
        Results.append(Result[0])

    if True in Results:
        index = Results.index(True)
        file_loc='./dataset/'+knownNames[index]
        os.chdir(file_loc)
        cv2.imwrite(filename, image1)
    else:
        name = input("Write the name of the Person: ")
        if len(name)>=2:
            os.mkdir('./dataset/'+name)
            os.chdir('./dataset/'+name)
            cv2.imwrite(filename,image1)
        else: 
            os.mkdir('./dataset/unknown')
            os.chdir('./dataset/unknown')
            cv2.imwrite(filename,image1)
    
    return knownNames,Results
