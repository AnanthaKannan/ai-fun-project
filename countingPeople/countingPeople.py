import cv2

faceCascade = cv2.CascadeClassifier("resource/haarcascade_frontalface_default.xml")

path = "resource/people.mp4"
cap = cv2.VideoCapture(path)

while True:
    _, img = cap.read()
    imgResult = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=8)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    allImg = cv2.hconcat([img, imgResult])
    cv2.imshow("Image", img)
    cv2.waitKey(10)