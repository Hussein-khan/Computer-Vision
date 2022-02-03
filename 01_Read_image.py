#import Dependencies
import cv2 as cv

#reading image
img = cv.imread('F:\\EDUCATION\Artificial Inteligence\\Artificial Intelligence & Data Science\\04 Computer Vision\\Resources\\01.jpg')

#show image
cv.imshow('picture',img)
cv.waitKey(0)