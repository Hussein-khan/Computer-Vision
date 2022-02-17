#import Dependencies
import cv2 as cv
from cv2 import circle
import matplotlib.pyplot as plt
import numpy as np
#reading image
img = cv.imread('Resources/07.jpg')

img1 = cv.resize(img,(800,600))

# gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

blank = np.zeros(img1.shape[:2],dtype='uint8')

circl = cv.circle(blank,(img1.shape[1]//2,img1.shape[0]//2),100,255,-1)

mask = cv.bitwise_and(img1,img1,mask=circl)

#show image
#cv.imshow('picture',gray)

# gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])
# plt.figure()
# plt.title('graph')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


plt.figure()
plt.title('Award')
plt.xlabel('Epochs')
plt.ylabel('Score')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img1],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    plt.legend(["1", "2","3"], loc ="lower right")
    print(hist)
plt.show()
#cv.imshow('img',img)
cv.waitKey(0)