#importing libraries
import cv2 as cv
import numpy as np

#webcam
cap = cv.VideoCapture(0)

#setting Web Cam
cap.set(10,100) #brightness
cap.set(3,640) #width
cap.set(4,480) #height

#displaying webcam
while True:
    ret,frame = cap.read()
    
    cv.imshow('webcam',frame)
    
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows
