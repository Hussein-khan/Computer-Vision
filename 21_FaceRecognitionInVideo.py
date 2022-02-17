#importing library
import cv2 as cv

#importing face detector file
faces_cascade = cv.CascadeClassifier('files/haarcascade_frontalface_default.xml')

#reading video
cap = cv.VideoCapture('Resources/vidd.mp4')

#playing video
while True:
    ret,frame = cap.read()

    #converting to grayscale
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    #using function
    faces = faces_cascade.detectMultiScale(gray,1.1,6)

    #tracking face
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    #showing image
    cv.imshow('video',frame)

    if cv.waitKey(1) & 0xFF==ord('d'):
        break
#cap
cap.release()
cv.destroyAllWindows()