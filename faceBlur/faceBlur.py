import time

import cv2

faceCascade = cv2.CascadeClassifier("C:/personal/ai-fun-project/basic/resource/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    imgResult = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # crop the face
        roi = imgResult[y:y + h, x:x + w]
        cv2.imshow("roi", roi)
        # applying a gaussian blur over this new rectangle area
        roi = cv2.GaussianBlur(roi, (23, 23), 30)
        # impose this blurred image on original image to get final image
        imgResult[y:y + roi.shape[0], x:x + roi.shape[1]] = roi

    allImg = cv2.hconcat([img, imgResult])
    cv2.imshow("Image", allImg)
    cv2.waitKey(1)