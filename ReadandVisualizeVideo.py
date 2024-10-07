import cv2
import os


#read video
video_path=os.path.join('.','10.mp4')
video=cv2.VideoCapture(video_path)



#visualize video
ret=True
while ret:
   ret,frame= video.read() 
   if ret:#we will be reading the frame from the video
    cv2.imshow('frame of videos',frame)
    cv2.waitKey(40)  
   #25 fps means we have 1/25 we 40 milliseconds will change frame after every 40ms
   video.release()
   cv2.destroyAllWindows()