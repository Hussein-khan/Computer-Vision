#importing libraries
import cv2 as cv

#webcam
cap = cv.VideoCapture(0)

#displaying webcam
while True:
    ret,frame = cap.read()
    
    cv.imshow('webcam',frame)

    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows
