#importing libraries
import cv2 as cv

#webcam
cap = cv.VideoCapture(0)

#displaying webcam
while True:
    ret,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binary) = cv.threshold(frame,127,255,cv.THRESH_BINARY)
    cv.imshow('webcam',frame)
    cv.imshow('gray',gray)
    cv.imshow('bNw',binary)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows
