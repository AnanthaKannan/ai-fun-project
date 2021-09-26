import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
# hue min, sat min, val min, hue max, sat min, val min
myColors = [[6, 147, 255, 61, 255, 255], [43, 148, 88, 147, 255, 255]]
# orange, blue (BGR)
myColorValues = [[72, 109, 248], [178, 80, 33]]
#
myPoints = [] ## [x, y, colorIdx]

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    index = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValues[index], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, index])
        index += 1
    return newPoints

def getContours(mask):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x, y, w, h = 0, 0, 0, 0
    if len(contours) != 0:
        for contour in contours:
            print(cv2.contourArea(contour))
            if cv2.contourArea(contour) > 500:
                # -1 used to draw all the contours
                # cv2.drawContours(imgResult, contours, -1, (0, 0, 255), 3)
                # True represented whether the image closed or no
                peri_meter = cv2.arcLength(contour, True)
                # to find out the corner points
                resolution = 0.03 * peri_meter
                approxCornoer = cv2.approxPolyDP(contour, resolution, True)
                cornerCount = len(approxCornoer)
                x,y,w,h = cv2.boundingRect(approxCornoer)
    return x+w//2, y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newPoint in newPoints:
            myPoints.append(newPoint)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow("Image", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break