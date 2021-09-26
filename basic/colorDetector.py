import cv2
import numpy as np

def empty(a):
    pass

"create track bar always this values statr from zero"
windowName = "TrackBars"
cv2.namedWindow(windowName)
cv2.resizeWindow(windowName, 640, 240)
cv2.createTrackbar("Hue Min", windowName, 0, 179, empty)
cv2.createTrackbar("Hue Max", windowName, 146, 179, empty)
cv2.createTrackbar("Sat Min", windowName, 0, 255, empty)
cv2.createTrackbar("Sat Max", windowName, 94, 255, empty)
cv2.createTrackbar("Val Min", windowName, 0, 255, empty)
cv2.createTrackbar("Val Max", windowName, 140, 255, empty)

def createRectForMask(mask, img):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        for contour in contours:
            print(cv2.contourArea(contour))
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x+h, y+h), (0, 0, 255), 3)

while True:
    img_ = cv2.imread("./resource/lambo.jpg")
    reHeight, reWidth = 300, 420
    img = cv2.resize(img_, (reWidth, reHeight))

    # get the value from track bar * the name should be same
    h_min = cv2.getTrackbarPos("Hue Min", windowName)
    h_max = cv2.getTrackbarPos("Hue Max", windowName)
    s_min = cv2.getTrackbarPos("Sat Min", windowName)
    s_max = cv2.getTrackbarPos("Sat Max", windowName)
    v_min = cv2.getTrackbarPos("Val Min", windowName)
    v_max = cv2.getTrackbarPos("Val Max", windowName)
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow("imgHSV", imgHSV)
    cv2.imshow("mask", mask)
    createRectForMask(mask, img)
    cv2.imshow("Image", img)
    cv2.imshow("imgResult", imgResult)
    cv2.waitKey(1)