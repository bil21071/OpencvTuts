#How do we develop the edge detector in the opencv 
#one is sobel operator other is the laplace operator
import os

import cv2
import numpy as np
img = cv2.imread(os.path.join('.', 'a1.jpg'))
#canny edge detector
img_edge=cv2.Canny(img,100,200) #trial and error
img_edge_delayed=cv2.dilate(img_edge,np.ones((5,5),dtype=np.int8)) #dilate is a fuction to make things thicker edge thicker
img_edge_erode=cv2.erode(img_edge_delayed,np.ones((5,5),dtype=np.int8))
#with erode  we are making everthing thinner opposite of dilate all use the numpy arrays
cv2.imshow('img', img)
cv2.imshow('img1', img_edge)
cv2.imshow('img2', img_edge_delayed)
cv2.imshow('img3', img_edge_erode)
cv2.waitKey(0)
# logic behind the detection technique is simple: preprocess the image, calculate the gradient values of the pixels in the image, apply a suppression algorithm followed by a double threshold, 
# and track weak edges using the hysteresis algorithm
