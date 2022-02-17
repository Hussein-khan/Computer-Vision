# changing the perspective of an image 

import cv2 as cv
import numpy as np

#reading image 
img = cv.imread('Resources/fb_img.jpg')
print(img.shape)
#defining points
point1 = np.float32([[198,157],[162,579],[626,190],[589,615]])

width = 835
height = 720

point2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv.getPerspectiveTransform(point1,point2)
out_img = cv.warpPerspective(img,matrix,(width,height))

cv.imshow('orignal',img)
cv.imshow('transform',out_img)
cv.waitKey(0)
cv.destroyAllWindows()