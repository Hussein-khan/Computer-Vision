#importing library
import cv2 as cv

#reading video
cap = cv.VideoCapture('Resources/vid.mp4')

#writing video
fourcc = cv.VideoWriter_fourcc(*'MJPG')
out = cv.VideoWriter('output.avi',fourcc,30,(640,480),isColor=True)
#playing video
while True:
    ret,frame = cap.read()
    frame = cv.resize(frame,(800,600))
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binary) = cv.threshold(frame,127,255,cv.THRESH_BINARY)
    
    if ret == True:
        #print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        #print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        cv.imshow('webcam',frame)

    
    #displaying video
        if cv.waitKey(1) & 0xFF==ord('q'):
            break

cap.release()
out.release()
cv.destroyAllWindows()