import cv2
import HandTrackingModule


hm = HandTrackingModule.handDedector(maxHands=1)

class handPostion:

    def getPlace(self, img, key):
        positon = hm.findPositon(hm.findHands(img))
        text = ""
        if len(positon) > 0:
            # print(positon[5], positon[8])
            cx_5, cy_5 = positon[5][1:]
            cx_8, cy_8 = positon[8][1:]
            # print(cx_5, cy_5, cx_8, cy_8)

            if cx_5 > cy_5 and cx_8 > cy_8:
                key = 119 #"top"
                text = "top"
            elif cx_5 > cy_5 and cx_8 < cy_8:
                key = 97 #"left"
                text = "left"
            # elif cx_5 < cy_5 and cx_8 < cy_8:
            #     text = "right"
        cv2.putText(img, text, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        return key

def main():
    hd = handPostion()
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()
        img = cv2.flip(img, 1)

        text = hd.getPlace(img, 'd')
        cv2.imshow("image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()