import cv2
#read webcam
webcam=cv2.VideoCapture(0) #0 is the webcam values 
#visualize the webcam
while True:      #we have never reach the end in the webcam since it keep increasing
    ret, frame=webcam.read()
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(40)  & 0XFF == ord('q'):    #if user press any error key so it will break or q
        break  
    #Like is the memory of the webcam q

webcam.release()
cv2.destroyAllWindows()
#They process very slow 
