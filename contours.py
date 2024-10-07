import os
import cv2


img=cv2.imread(os.path.join('.','birds.jpg'))
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)   #127 is threshold value below it will be zero above it will be 1 
#we want to take 1 if it below the threshold which is 127 and we want to take it as 0
coutours,heirchary=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in coutours:
    if cv2.contourArea(cnt) >200:
        cv2.drawContours(img,cnt,-1,(0,255,0),1) 
        
        x1,y1,w,h=cv2.boundingRect(cnt)
        cv2.rectangle(img,(x1,y1),(x1+w,y1+w),(0,255,0),2)
        #bounding rect is the contour detector of the bounder boxes of top left corner
        #xy co-ordinates and the bottom left corner of the xy-co-ordinates
        #we want to draw the contour on the image who area is greater than 200
    #we want the contours
    #we are calculating the contours
#we need images with one channel
cv2.imshow('img',img)
cv2.imshow('img1.0',img_gray)
cv2.imshow('img1',thresh)
cv2.waitKey(0)
#when we working with contours we will work with the isolated white regions in the imahge 
#we need binary image in this to convert this global 
#that why we use the binary threshold
#we need the white objects
#now we know the contours applying it to the image 
#ideally each element is one of these region all 
# the border of all the isolated region of these images 
#they are isolated with them for iamges for isolated white regions 
'''

What are contours? Contours can be explained simply as a curve joining 
all the continuous points (along the boundary), 
having same color or intensity. 
The contours are a useful tool for shape analysis and object detection and recognition.
For better accuracy, use binary images.
'''
#we are drawing the contours border on the real images whose area is greater than 200
#all the border contoutrs of all the diffirent fields 

 #dimensionality the channels depend on photoreceptor cell the human
 #body has 3 receptor cell rgb