import os
import cv2



#read_image
image_path =os.path.join('.','BIRD.jpg') #current directory, data folder,filename

img=cv2.imread(image_path)


#write_image
cv2.imwrite(os.path.join('.','BIRD_out.jpg'),img)


#visualize image
cv2.imshow('image',img)  #image is the label and the image img is the image we are reading
cv2.waitKey(0)  #it used to wait to number is in Milliseconds