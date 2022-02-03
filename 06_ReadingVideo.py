#importing library
import cv2 as cv

#reading video
cap = cv.VideoCapture('F:\\EDUCATION\Artificial Inteligence\\Artificial Intelligence & Data Science\\04 Computer Vision\Resources\\vid.mp4')

#playing video
while True:
    ret,frame = cap.read()

    cv.imshow('video',frame)

    if cv.waitKey(1) & 0xFF==ord('d'):
        break

cap.release()
cv.destroyAllWindows()