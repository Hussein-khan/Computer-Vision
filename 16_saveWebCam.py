#importing library
import cv2 as cv
import numpy as np

#read webcam
cap = cv.VideoCapture(0)

#writing video
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('out.mp4',fourcc,30,(1280,720))

#setting resolution
cap.set(3,1280)
cap.set(4,720)

#display webcam
while True:
    ret,frame = cap.read()
    if ret == True:
        #print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        #print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        
        cv.imshow('webcam',frame)
        out.write(frame)

        if cv.waitKey(1) & 0xFF==ord('q'):
            break
cap.release()
cv.destroyAllWindows()