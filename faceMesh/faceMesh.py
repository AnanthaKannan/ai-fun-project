import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

while True:
    _, img = cap.read()
    f = 1.3 #0.30
    img = cv2.resize(img, dsize=(0, 0), fx=f, fy=f)
    # only RGB can access
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION, drawSpec, drawSpec)

            landmark = faceLms.landmark
            print(landmark)

    # for id, lm in enumerate(faceLms.landmark):
    #     ih, iw, ic = img.shape
    #     x,y = int(lm.x*iw), int(lm.y*ih)

    cv2.imshow('Img', img)
    cv2.waitKey(1)