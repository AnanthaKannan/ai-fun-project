import sys
sys.path.insert(0, '../ai-fun-project')

import cv2
import HandTrackingModule
import numpy as np

hm = HandTrackingModule.handDetector(maxHands=1)

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

linePoints = []
lenSnake = 60

def createFollowedLine():
    for point in linePoints:
        # cv2.circle(img, (point[0], point[1]), 8, (0, 0, 255), -1)
        isClosed = False
        pts = np.array([linePoints], np.int32)
  
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], isClosed, (0, 0, 255), 8)


def createLinePoints(x, y):
    global linePoints

    if len(linePoints) > lenSnake:
        linePoints = linePoints[len(linePoints)-lenSnake:]

    addValue = True
    for point in linePoints:
        if point[0] == x or point[1] == y:
            addValue = False
        
    if addValue == True:
        linePoints.append([x, y])

        

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    img = hm.findHands(img, draw=False)
    lmList = hm.findPosition(img, draw=False)
    if len(lmList) > 0:
        i, x, y = lmList[8]
        cv2.circle(img, (x, y), 15, (0, 0, 255), -1)
        createLinePoints(x, y)

    createFollowedLine()
    cv2.imshow("Image", img)

    cv2.waitKey(1)