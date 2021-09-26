# pip install opencv-contrib-python==3.4.13.47
import cv2


cap = cv2.VideoCapture(0)
# tracker = cv2.TrackerMOSSE_create()
tracker = cv2.TrackerCRST_create() # low speed but accuracy high

_, img = cap.read()
img = cv2.flip(img, 1)
bbox = cv2.selectROI("Tracking", img, False)
print(bbox)
tracker.init(img, bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2, 1)

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    _, bbox = tracker.update(img)

    if _:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Lost", (70, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)


    cv2.imshow("Tracking", img)

    cv2.waitKey(1)