import cv2
import numpy as np
"""
to create a black image
512 means it is 512 pixels w*h
3 means three channal
"""

img = np.zeros((512, 512, 3))
print(img.shape)

""" make the image as blue"""
# img[:] = 255, 0, 0
"""make the color in between place"""
# img[200:300, 100:300] = 255, 255, 0

"create line"
lineStartPoint = (0, 0)
lineEndPoint = (300, 300)
lineColor = (0, 255, 0)
lineThickness = 3
cv2.line(img, lineStartPoint, lineEndPoint, lineColor, lineThickness)

"create rectangle"
recStartPoint = (0, 0)
recEndPoint = (250, 350)
recColor = (0, 0, 255)
recThickness = 2
cv2.rectangle(img, recStartPoint, recEndPoint, recColor, recThickness)

"create circle"
centerPoint = (400, 50) # from the left 400 and from the top 50
radios = 30
circleColor = (255, 0, 0)
circleThickness = 2
cv2.circle(img, centerPoint, radios, circleColor, circleThickness)

"add text in image"
text = "Open CV"
txtOrigin = (300, 200)
textFont = cv2.FONT_HERSHEY_COMPLEX
txtScale = 1
txtColor = (0, 150,0)
txtThickness = 2
cv2.putText(img, text, txtOrigin, textFont, txtScale, txtColor, txtThickness)

cv2.imshow("Image", img)
cv2.waitKey(0)