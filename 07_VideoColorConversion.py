#importing library
import cv2 as cv

#reading video
cap = cv.VideoCapture('F:\\EDUCATION\Artificial Inteligence\\Artificial Intelligence & Data Science\\04 Computer Vision\\Resources\\vid.mp4')

#playing video
while True:
    ret,frame = cap.read()
    frame = cv.resize(frame,(800,600))
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binary) = cv.threshold(frame,127,255,cv.THRESH_BINARY)
    cv.imshow('video',gray)
    cv.imshow('rangeen',frame)
    cv.imshow('kala',binary)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()