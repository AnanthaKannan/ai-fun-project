import cv2

# to read and show the image
capImg = cv2.imread("resource/dynamoDb1.PNG")
reHeight, reWidth = 200, 300
imgResize = cv2.resize(capImg, (reWidth, reHeight))
cv2.imshow('image', imgResize)

# to read and show the video
cap = cv2.VideoCapture(0) # if you have camera you can give 0, if not you can give the video path here

cap.set(3, 640) # set the width
cap.set(4, 480) # set the height
cap.set(10, 1000) # set the brightness

while True:
    _, img = cap.read()
    cv2.imshow("video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
