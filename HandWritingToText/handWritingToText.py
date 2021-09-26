import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

def readText(img):
    reader = easyocr.Reader(['en'], gpu=True)
    result = reader.readtext(img)
    # print(result)
    textList = []
    for detection in result:
        top_left = tuple([int(val) for val in detection[0][0]])
        bottom_right = tuple([int(val) for val in detection[0][2]])
        text = detection[1]
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        textList.append(text)
        cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
        print(text, top_left, bottom_right)
    return textList

def createGraph():
    x = [0, 1, 2, 3, -2, -1]
    y = [0, 1, 2, 3, -2, -1]
    print(x, y)
    plt.plot(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('My first graph!')
    plt.show()


path = "imgV3.jpeg"
# path = "black_board.mp4"
# cap = cv2.VideoCapture(path)

while True:
    img = cv2.imread(path)
    # _, img = cap.read()
    f = 1
    img = cv2.resize(img, dsize=(0, 0), fx=f, fy=f)
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    # it will give output just like mask
    # imgCanny = cv2.Canny(imgGray, 150, 150)

    textList = readText(img)
    # print(textList)
    cv2.imshow("Image", img)
    # createGraph()
    cv2.waitKey(1)