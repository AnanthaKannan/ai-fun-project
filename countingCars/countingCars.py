import cv2
import numpy as np

def sort_contours(contours):
    # construct the list of bounding boxes and sort them from top to bottom
    boundingBoxes = [cv2.boundingRect(c) for c in contours]
    (contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes)
       , key=lambda b: b[1][0], reverse=False))
    # return the list of sorted contours
    return contours

def createRectForMask(mask, img):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sort_contours(contours)
    if len(contours) != 0:
        count = 0
        for contour in contours:
            contourArea = cv2.contourArea(contour)
            # print(contourArea)
            if contourArea > 300:
                # print("contourArea", contourArea)
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # # -1 used to draw all the contours
                # cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
                count += 1
                cv2.putText(img, str(count), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
        cv2.putText(img, str(count), (10, 60), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 2)


def createMask(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min, h_max, s_min, s_max, v_min, v_max = 12, 85, 53, 255, 0, 255
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    return mask

cap = cv2.VideoCapture("resource/chairs.mp4")

while True:
    # img = cv2.imread("resource/chairs.jpg")
    _, img = cap.read()
    resize = 1.5
    img = cv2.resize(img, dsize=(0, 0), fx=resize, fy=resize)
    mask = createMask(img)

    # cv2.imshow("Img", mask)
    createRectForMask(mask, img)
    finalImg = cv2.vconcat([img])
    cv2.imshow("Img", finalImg)
    if cv2.waitKey(13) & 0xFF == ord('q'):
        break


