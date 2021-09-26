import time
import cv2

faceCascade = cv2.CascadeClassifier("cars.xml")
cap = cv2.VideoCapture("carsInAndOut.mp4")

while True:
    _, img = cap.read()
    img = cv2.resize(img, )
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # crop the face
        # applying a gaussian blur over this new rectangle area

    cv2.imshow("Image", img)
    cv2.waitKey(1)