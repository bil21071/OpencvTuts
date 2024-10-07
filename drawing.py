import os
import cv2
#we will be drawing on the image 
img=cv2.imread(os.path.join('.','whiteboard.png'))
print(img.shape)
#line
#to draw a line on top of the image
cv2.line(img,(671,1000),(300,450),(0,253,0),3)  #starting and ending point of lines 2 co-ordinates x and y co ordinate

#line is most important
#rectangle 
cv2.rectangle(img,(200,350),(450,600),(0,0,255),10)  #last is the value of thinkness
# in negative case of thickness will be field -1


#circle 
800
cv2.circle(img,(750,230),150,(255,0,0),10)   #  the 15 is the radius of the circle
#greater the radius the greater will be the circle 
#text 

cv2.putText(img,'Hello you!',(500,450),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),10)    #fonts of the text are available
#thickness and size of text to be specify 

cv2.imshow('img',img)
cv2.waitKey(0)