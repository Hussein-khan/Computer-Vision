#impoert dependencies
import cv2 as cv
import numpy as np

#read orignal image
img1 = cv.imread("Resources/01.jpg")
#resize image
img2 = cv.resize(img1,(600,400))
#gray conversion
img3 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
#blur image 
img4 = cv.GaussianBlur(img3,(7,7),0)
#edge detection 
img5 = cv.Canny(img2,30,30)
#thickness of line 
img6 = cv.dilate(img5,(5,10),iterations=2)
#image erosion
img7 = cv.erode(img6,(7,7),iterations=2)
#black and white image 
thresh,img8 = cv.threshold(img2,127,200,cv.THRESH_BINARY)
#cropping image
img9 = img2[0:500,0:500]

cv.imshow('pic1',img1)
cv.imshow('pic2',img2)
cv.imshow('pic3',img3)
cv.imshow('pic4',img4)
cv.imshow('pic5',img5)
cv.imshow('pic6',img6)
cv.imshow('pic7',img7)
cv.imshow('pic8',img8)
cv.imshow('pic9',img9)
cv.waitKey(0)
cv.destroyAllWindows()
print(img1.shape)