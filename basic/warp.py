import cv2
import numpy as np

img = cv2.imread("./resource/dynamoDb1.PNG")

leftTop = [114, 203]
leftBottom = [115, 326]
rightTop = [297, 206]
rightBottom = [296, 329]

width, heigt = 181, 123
pts1 = np.float32([leftTop, rightTop, leftBottom, rightBottom])
pts2 = np.float32([[1,0], [width, 0], [0, heigt], [width, heigt]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOut = cv2.warpPerspective(img, matrix, (width, heigt))


cv2.imshow('img', img)
cv2.imshow("imgOut", imgOut)
cv2.waitKey(0)