#import Dependencies
import cv2 as cv

#reading image
img = cv.imread('F:\\EDUCATION\\Artificial Inteligence\\Computer Vision\\Resources\\01.jpg')
img1 = cv.resize(img,(800,600))
#show image
cv.imshow('picture',img1)
cv.waitKey(0)