import cv2

img = cv2.imread("./resource/dynamoDb1.PNG")

"""
Basically the images are array. so you need to 
select the specific array to crop the images

1. the first value is height
2. the secound value is height
"""
imgCropped = img[0:300, 300: 600]
cv2.imshow("img", img)
cv2.imshow("imgCropped", imgCropped)
cv2.waitKey(0)