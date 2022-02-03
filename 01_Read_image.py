#import Dependencies
import cv2 as cv

#reading image
img = cv.imread('F:\\EDUCATION\\Artificial Inteligence\\Computer Vision\\Resources\\image1.png')

#show image
cv.imshow('picture',img)
cv.waitKey(0)