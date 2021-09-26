# https://www.geeksforgeeks.org/concatenate-images-using-opencv-in-python/
import cv2
import numpy as np

img = cv2.imread("./resource/shapes.png")

""""
vconcat = concat the image in vertical
hconcat = concat the image in horizontal
"""

def stackImg(list_2d, resize=1):
    stackImgs = cv2.vconcat([cv2.hconcat(list_h)
                        for list_h in list_2d])
    return cv2.resize(stackImgs, dsize=(0, 0), fx=resize, fy=resize)

allImg = stackImg([[img, img], [img, img]], resize=0.8)
cv2.imshow("ImgVer", allImg)
cv2.waitKey(0)