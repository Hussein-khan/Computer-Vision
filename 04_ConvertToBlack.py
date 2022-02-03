#import Dependencies
import cv2 as cv

#reading image
img = cv.imread('F:\\EDUCATION\\Artificial Inteligence\\Computer Vision\\Resources\\01.jpg')
img1 = cv.resize(img,(800,600))
img1 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

#conversion
(thresh,binary) = cv.threshold(img1,127,255,cv.THRESH_BINARY)


#show image
cv.imshow('gray',img1)
cv.imshow('picture',binary)
cv.waitKey(0)
cv.destroyAllWindows()