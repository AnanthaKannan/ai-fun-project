import cv2
# from pygame import mixer
import numpy as np

cap = cv2.VideoCapture(0)
# cap.set(3, 1920)
# cap.set(4, 1080)

# Importing drum beats and images
# drumImg = cv2.imread("chairs.jpg")
# mixer.init()
# drum_hat = mixer.Sound('./sounds/high_hat_1.ogg')
# drum_snare = mixer.Sound('./sounds/snare_1.wav')
# drum_snare.play()
# drum_hat.play()
ox, oy = 200, 200

def createRectForMask(mask, img):
    contours, hierarchy, _s = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print(_s)
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
    # h_min, h_max, s_min, s_max, v_min, v_max = 20, 179, 201, 255, 33, 255
    h_min, h_max, s_min, s_max, v_min, v_max = 12, 85, 53, 255, 0, 255
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    return mask



while True:
    _, img = cap.read()
    # img = cv2.flip(img, 1)
    # h, w, channel = drumImg.shape

    mask = createMask(img)
    # cv2.imshow("mask", mask)
    createRectForMask(mask, img)
    # img[oy:oy + h, ox:ox + w] = drumImg
    cv2.imshow("Image", img)
    cv2.waitKey(1)