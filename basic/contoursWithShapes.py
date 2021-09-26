import cv2


def createRectForMask(mask, img):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        print("contoursCount", len(contours))
        for contour in contours:
            print(cv2.contourArea(contour))
            if cv2.contourArea(contour) > 100:
                x, y, w, h = cv2.boundingRect(contour)
                # -1 used to draw all the contours
                cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

                # True represented whether the image closed or no
                peri_meter = cv2.arcLength(contour, True)
                # to find out the corner points
                resolution = 0.03 * peri_meter
                approxCornoer = cv2.approxPolyDP(contour, resolution, True)
                print(len(approxCornoer))
                cornerCount = len(approxCornoer)
                x,y,w,h = cv2.boundingRect(approxCornoer)

                if cornerCount == 3: objectType = "Tri"
                elif cornerCount == 4:
                    aspRatio = w/float(h)
                    if aspRatio > 0.95 and aspRatio < 1.05: objectType = "Square"
                    else: objectType = "Rect"
                elif cornerCount > 4:
                    print("circleCount", cornerCount)
                    objectType = "Circle"
                else: objectType="None"

                cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
                centerPoint = (x+(w//2)-10, y+(h//2)-10)
                cv2.putText(img, objectType, centerPoint, cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)


img = cv2.imread("./resource/shapes.png")
imgContours = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
# it will give output just like mask
imgCanny = cv2.Canny(imgBlur, 50, 50)

createRectForMask(imgCanny, imgContours)
cv2.imshow("image", img)
cv2.imshow("imgCanny", imgCanny)
cv2.imshow("imgContours", imgContours)
cv2.waitKey(0)