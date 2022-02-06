#importing library
import cv2 as cv
import numpy as np

#read webcam
cap = cv.VideoCapture(0)

#setting resolution
cap.set(3,1280)
cap.set(4,720)

#display webcam
while True:
    ret,frame = cap.read()   
        
    cv.imshow('webcam',frame)
        
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()