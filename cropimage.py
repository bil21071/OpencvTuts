#crop
import os
import cv2


img=cv2.imread(os.path.join('.','BIRD.jpg'))
print(img.shape)

cropped_img=img[110:370,110:550] #height and widht   first specify the height and the then widht

cv2.imshow('image',img)
cv2.imshow('image1',cropped_img)
cv2.waitKey(0)