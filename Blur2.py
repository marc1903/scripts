import cv2
import os
from PIL import Image
import numpy as np
#
#
# import os
#
# path = "./../Img_Pessoas"
#
# for filename in os.listdir(path):
#     #name, ext = os.path.splitext(filename)
#     print(filename)

diretorio = '/home/davint-1/Desktop/Marc/pedestrian_ANN/testImages'
arquivos = os.listdir(diretorio)

count = 0

for a in arquivos:
    if a.lower().endswith('.jpg') or a.lower().endswith('.png') or a.lower().endswith('.jpeg'):

        image = cv2.imread(diretorio + '/' + a)
        result_image = image.copy()

        # Specify the trained cascade classifier
        face_cascade_name = "./haarcascade_frontalface_alt.xml"
        face_cascade_name2 = "./haarcascade_profileface.xml"

        # Create a cascade classifier
        face_cascade = cv2.CascadeClassifier()
        face_cascade2 = cv2.CascadeClassifier()

        # Load the specified classifier
        face_cascade.load(face_cascade_name)
        face_cascade2.load(face_cascade_name2)

        #Preprocess the image
        grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #grayimg = cv2.equalizeHist(grayimg, grayimg)




        #Run the classifiers
        # faces = face_cascade.detectMultiScale(grayimg, 1.1, 2, 0|cv2.CASCADE_SCALE_IMAGE, (10, 10))
        # faces2 = face_cascade2.detectMultiScale(grayimg, 1.1, 2, 0|cv2.CASCADE_SCALE_IMAGE, (10, 10))

        faces = face_cascade.detectMultiScale(grayimg,scaleFactor=1.1, minNeighbors=7, minSize=(10,10), flags=cv2.CASCADE_SCALE_IMAGE)
        faces2 = face_cascade2.detectMultiScale(grayimg,
        scaleFactor=1.1, minNeighbors=7, minSize=(10,10), flags=cv2.CASCADE_SCALE_IMAGE)

        print ("Faces detected")
        count += 1
        print(count)

        if len(faces) != 0:         # If there are faces in the images
            for f in faces:         # For each face in the image

        # Get the origin co-ordinates and the length and width till where the face extends
                x, y, w, h = [ v for v in f ]

        # get the rectangle img around all the faces
                cv2.rectangle(image, (x,y), (x+w,y+h), (255,255,255), 5)
                sub_face = image[y:y+h, x:x+w]
        # apply a gaussian blur on this new recangle image
                sub_face = cv2.GaussianBlur(sub_face,(23, 23), 30)
        # merge this blurry rectangle to our final image
                result_image[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face
                face_file_name = "./face_" + str(y) + ".jpg"
                cv2.imwrite(face_file_name, sub_face)

        if len(faces2) != 0:         # If there are faces in the images
            for f in faces2:         # For each face in the image

        # Get the origin co-ordinates and the length and width till where the face extends
                x, y, w, h = [ v for v in f ]

        # get the rectangle img around all the faces
                cv2.rectangle(image, (x,y), (x+w,y+h), (255,255,255), 5)
                sub_face = image[y:y+h, x:x+w]
        # apply a gaussian blur on this new recangle image
                sub_face = cv2.GaussianBlur(sub_face,(23, 23), 30)
        # merge this blurry rectangle to our final image
                result_image[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face
                face_file_name = "./face_" + str(y) + ".jpg"
                cv2.imwrite(face_file_name, sub_face)

        # if a.lower().endswith('.jpeg'):
        #     aux = len(a) - 5
        #
        # else:
        #     aux = len(a) - 4
        #
        # novoNome = a[:aux]

        #cv2.imshow("Detected face", result_image)
        cv2.imwrite("/home/davint-1/Desktop/Marc/pedestrian_ANN/result/" + a, result_image)