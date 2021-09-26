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

def getMask(img, imgHSV):
    # get the value from track bar * the name should be same
    h_min = cv2.getTrackbarPos("Hue Min", windowName)
    h_max = cv2.getTrackbarPos("Hue Max", windowName)
    s_min = cv2.getTrackbarPos("Sat Min", windowName)
    s_max = cv2.getTrackbarPos("Sat Max", windowName)
    v_min = cv2.getTrackbarPos("Val Min", windowName)
    v_max = cv2.getTrackbarPos("Val Max", windowName)
    # print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    return [mask, imgResult]


cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    # img = cv2.imread("resource/cars.png")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    "to get the mask and applied mask images"
    maskArr = getMask(img, imgHSV)
    mask = maskArr[0]
    """covert single channel to 3 channel"""
    threeChannelMask = cv2.merge((mask, mask, mask))

    hImg = cv2.hconcat([img, threeChannelMask, maskArr[1]])
    resize = 0.7
    resizeImg = cv2.resize(hImg, dsize=(0, 0), fx=resize, fy=resize)
    cv2.imshow("concatImg", resizeImg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
