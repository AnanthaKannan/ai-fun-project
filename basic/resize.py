import cv2

img = cv2.imread("./resource/dynamoDb1.PNG")

height, width, channel = img.shape
print("orginalImgShape", height, width, channel)

# to resize
reHeight, reWidth = 200, 300
imgResize = cv2.resize(img, (reWidth, reHeight))
print("updatedImgShape", imgResize.shape)

cv2.imshow("img", img)
cv2.imshow('imgResize', imgResize)
cv2.waitKey(0)