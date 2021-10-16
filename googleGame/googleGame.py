import cv2
import HandTrackingModule
import pyautogui


hm = HandTrackingModule.handDetector(maxHands=1)

cap = cv2.VideoCapture(0)


def findDistance(lmList):
    i2, x1, y1 = lmList[4]
    i1, x2, y2 = lmList[8]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 130), 3, cv2.RETR_EXTERNAL)
    cv2.circle(img, (x1, y1), 2, (100, 200, 100), 3)
    cv2.circle(img, (x2, y2), 2, (100, 200, 100), 3)
    distance = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
    if distance < 40:
         print('jump')
         cv2.line(img, (x1, y1), (x2, y2), (244, 255, 130), 3, cv2.RETR_EXTERNAL)
         cv2.putText(img, "JUMP", (10, 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (230, 210, 200), 2)
         pyautogui.press("up")
    else:
        print('no jump')


while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    img = hm.findHands(img, draw=False)
    lmList = hm.findPosition(img)
    if len(lmList) > 0:
        findDistance(lmList)
    cv2.imshow("Image", img)

    cv2.waitKey(1)
