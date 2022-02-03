#importing libraries
import cv2 as cv

#webcam
cap = cv.VideoCapture(0)

#saving
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.mp4',fourcc,20.0,(640,480))

#displaying webcam
while True:
    ret,frame = cap.read()
    if ret == True:
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        cv.imshow('webcam',frame)

        if cv.waitKey(1) & 0xFF==ord('q'):
            break

cap.release()
out.release()
cv.destroyAllWindows()
