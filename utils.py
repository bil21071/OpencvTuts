import numpy as np
import cv2

def get_limits(color):
    c=np.uint8([[color]]) #here insert the bgr value which you want to convert to hsv
    hsvC=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    
    Lowerlimit=hsvC[0][0][0] - 10,100,100
    UpperLimit=hsvC[0][0][10]+ 10,255,255
    
    Lowerlimit=np.array(Lowerlimit,dtype=np.uint8)
    UpperLimit=np.array(UpperLimit,dtype=np.uint8)
    
    return Lowerlimit,UpperLimit

#Much easier and simpler