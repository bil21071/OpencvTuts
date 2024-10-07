#in opencv there are two types of thresholding one is the normal thresholding and 
#other is the deep thresholding  global threshold
import os
import cv2
img=cv2.imread(os.path.join('.','bear.jpg'))
#image thresholding is basically used for creating the binary images
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY)  #under below value 80 will be 0 and above 80 to 255 as 1
thresh=cv2.blur(thresh,(10,10))
ret,thresh=cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY) 
cv2.imshow('image',img_gray)
cv2.imshow('i',thresh)
cv2.waitKey(0)