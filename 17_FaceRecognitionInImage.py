#importing libraries
import cv2 as cv

#importing face detector filr
faces_cascade = cv.CascadeClassifier('files/haarcascade_frontalface_default.xml')

#reading image
img = cv.imread('Resources/imgg.JPG')
img = cv.resize(img,(800,600))
#converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#using function
faces = faces_cascade.detectMultiScale(gray,1.1,6)

#tracking face
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()