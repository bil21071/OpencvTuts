#blur the remove the noise 
#blurring work on each block of pixels
#we are replacing the blur block pixel with it neighbourhood the average of all pixels
import os 
import cv2

# img=cv2.imread(os.path.join('.','work.jpg'))
# img=cv2.imread(os.path.join('.','a.jpg'))
k_size=3  #the size of the neighbour to calculate the average we can apply at diffirent coordinates
img_blur=cv2.blur(img,(k_size,k_size))  #it is the classical blur function more than enough common used
#increase size image more blur information otherwise best 
img_Gaussianblur=cv2.GaussianBlur(img,(k_size,k_size),5)  #Larger region
img_median_blur=cv2.medianBlur(img,k_size)
cv2.imshow('image',img)
cv2.imshow('image2',img_blur)
cv2.imshow('image3',img_Gaussianblur)
cv2.imshow('image4',img_median_blur)  #it is the median taking square of the nrighbour size
cv2.waitKey(0)

#There are 4 types of Blur
#we will remove the noise from the gray scale image
#still seeing the noise
#Check camera specification frames per second and it resolution