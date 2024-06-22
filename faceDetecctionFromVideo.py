import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture("sampleVideo.mp4")

while True:

    _, img = cap.read()

    faces = faceCascade.detectMultiScale(img)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("video",img)
    
    if cv2.waitKey(1) == 27:
        break


cv2.destroyAllWindows()
