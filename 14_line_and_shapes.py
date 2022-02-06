#drawline and shape 
import cv2 as cv
import numpy as np

#draw image 
img1 = np.zeros((600,600))
img2 = np.ones((600,600))

#print size 
print('size of an image is :',img1.shape)
print('size of an image is :',img2.shape)

#adding colors
colored_img = np.zeros((600,600,3),np.uint8) #adding color chanel
colored_img[:] = 243,0,200 #purple color on complete image
colored_img[0:300,200:300] = 175,45,0 #color the specific part of picture 

#draw line 
cv.line(colored_img,(0,0),(400,400),(0,255,155),3)
cv.line(colored_img,(0,0),(600,600),(0,0,255),3)

#draw rectangle
cv.rectangle(colored_img,(50,100),(400,400),(0,0,255),3)
cv.rectangle(colored_img,(150,100),(400,400),(0,0,255),cv.FILLED)

#adding circle
cv.circle(colored_img,(400,400),100,(255,0,0),3)

#adding text
cv.putText(colored_img,"husseinkhan",(100,500),cv.FONT_HERSHEY_DUPLEX,2,(0,255,0),2)

#display image 
cv.imshow('black',img1)
cv.imshow('white',img2)
cv.imshow('colored',colored_img)
cv.waitKey(0)
cv.destroyAllWindows()