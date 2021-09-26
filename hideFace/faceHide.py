import time
import cv2

faceCascade = cv2.CascadeClassifier("C:/personal/ai-fun-project/basic/resource/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

time.sleep(5)
bg = 0

for i in range(30):
    _, bg = cap.read()
    bg = cv2.flip(bg, 1)

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    imgResult = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # crop the face
        roi = bg[y:y + h, x:x + w]
        cv2.imshow("roi", roi)
        # impose this blurred image on original image to get final image
        imgResult[y:y + roi.shape[0], x:x + roi.shape[1]] = roi

    allImg = cv2.hconcat([img, imgResult])
    cv2.imshow("Image", allImg)
    cv2.waitKey(1)