import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("sampleGroupPhoto.jpg")

faces = faceCascade.detectMultiScale(img)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("photo",img)

cv2.waitKey()

cv2.destroyAllWindows()
