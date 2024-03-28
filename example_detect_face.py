#Importing OpenCV 
import cv2 
#Importing HARR CASCADE XML file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Capture Video from web cam hence (0) or else add your own media file
cap = cv2.VideoCapture(0)

#Creating a loop to capture each frame of the video in the name of Img
while True:
    _,img = cap.read()

    #Converting to grey scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Allowing multiple face detection
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)

    #Creating Rectangle around face
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 250), 2)
        # le x = bord gauche , w = largeur -> exprime la distance, donc centre = (x + w / 2, y + h / 2) 
        cv2.putText(img,str(x+w/2)+" - "+str(y+h/2),(90,90),cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    #Displaying the image 
    cv2.imshow('Detected Face Image',  img)

    #Waiting for escape key for image to close adding the break statement to end the face detection screen
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#Real-time releasing the captired frames
cap.release()
