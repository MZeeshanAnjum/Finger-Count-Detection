import os
import time 
import cv2
import matplotlib.pyplot as plt
import numpy as np
import hand_tracking_module as htm 
#picture=cv2.imread("D:\Finger detection\logo.PNG")
#picture = cv2.resize(picture, (100, 100))
#plt.imshow(picture)
#plt.show()
a=cv2.VideoCapture(0)
detector=htm.handDetector()
while(True):
    success,img=a.read()
    img= cv2.flip(img, 1)
    #IF YOU WANT TO ADD A PICTURE IN THE LIVE CAM DO THIS
    #img[0:100,0:100]=picture => ADD THE LOCATION OF THE LIVE CAM AND REPLACE THE PIXLES WITH THE IMAGE
    #cv2.putText(img,f"",(200,40),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)
    image=detector.findHands(img)
    lmList=detector.findPosition(img)
    tip_id=[8,12,16,20]#4 IS FOR THE THUMB, WE DIDNT USE THIS 
    fingers=[]
    #bottom_id=[6,10,14,18]
    if len(lmList)!=0:
        #THUMB IF ITS CX IS ON THE SIDE OF PINKY FINGER WE ASSUME ITS CLOSE AND ITS FOR THE RIGHT HAND RIGHT NOW
        
        if (lmList[4][1] > lmList[4-1][1] and lmList[4][3]=="Right"):
            fingers.append(1)
        elif(lmList[4][1] < lmList[4-1][1] and lmList[4][3]=="Left"):
            fingers.append(1)
        else:
            fingers.append(0)
        for i in tip_id:
            if (lmList[i][2] < lmList[i-1][2]):
                fingers.append(1)
            else:
                fingers.append(0)
        #print(fingers)
    cv2.putText(img, f"Option number: {(sum(fingers))} is Selected", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2.2,
                    (0, 255, 0), 3)
    cv2.imshow("img",image)
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    