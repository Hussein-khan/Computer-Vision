# coordinates of an image
import cv2 as cv 
import numpy as np

#define function

def find_coord(event,x,y,flags,params):

    if event == cv.EVENT_FLAG_LBUTTON:
        #left mouse click
        print(x,'',y)

        #define the same image
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img,str(x)+','+str(y),(x,y),font,1,(255,0,0),thickness=2)

        #show text
        cv.imshow('text',img)

#display function
if __name__ =="__main__":
    #reading image
    img = cv.imread('Resources/fb_img.jpg',1)
    cv.imshow('img',img)
    cv.setMouseCallback('img',find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()