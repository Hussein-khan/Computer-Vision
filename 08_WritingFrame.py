#importing library
import cv2 as cv

#reading video
cap = cv.VideoCapture('F:\\EDUCATION\\Artificial Inteligence\\Computer Vision\\Resources\\vid.mp4')

#writing video
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.mp4',fourcc,20.0,(640,480))
#playing video
while True:
    ret,frame = cap.read()
    frame = cv.resize(frame,(800,600))
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binary) = cv.threshold(frame,127,255,cv.THRESH_BINARY)
    
    if ret == True:
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        cv.imshow('webcam',frame)

    
    #displaying video
        if cv.waitKey(1) & 0xFF==ord('q'):
            break

cap.release()
out.release()
cv.destroyAllWindows()