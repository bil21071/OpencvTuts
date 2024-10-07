import os
import cv2

img=cv2.imread(os.path.join('.','BIRD.jpg'))
resizedimage=cv2.resize(img,(640,640))  #resizing the image widht 640 and height 480
print(img.shape)
print(resizedimage.shape)
cv2.imshow('image',img)
cv2.imshow('image1',resizedimage)
cv2.waitKey(0)
#it has 3 channels widht is 612 and height is 408
#(height,widht,channel) when shape is called 