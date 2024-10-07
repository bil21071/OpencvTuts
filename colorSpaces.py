import os 
import cv2

img=cv2.imread(os.path.join('.','BIRD.jpg'))#it is in bgr color space w  #it is the rgb image of red green blue has values
IMG_RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #it convert to another colorspace we have alot of color spaces
#we will convert the color space from bgr color space to the rgb color spaces 
IMG_GRAY=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('image',img)
cv2.imshow('image1',IMG_RGB)
cv2.imshow('image2',IMG_GRAY)
cv2.imshow('image3',img_hsv)
cv2.waitKey(0)   