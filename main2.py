import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np


width,height=1280,720
folderPath="Presentation"

#Variables
hs,ws=int(120*1),int(213*1)
imgNumber=0
gestureThreshold=300
buttonPressed=False
buttonCounter=0
buttonDelay=30
annotations=[]

#Adding the hand detector
detector=HandDetector(detectionCon=0.8,maxHands=1)


#Camera configuration
cap =cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)


#Get the list of presentation images
pathImages= sorted(os.listdir(folderPath),key=len)
# print(pathImages)



while True: 
    success,img=cap.read()
    #To move the image in the correct direction 
    img=cv2.flip(img,1)
    pathfullImage=os.path.join(folderPath,pathImages[imgNumber])
    imgcurrent=cv2.imread(pathfullImage)
    # w = imgcurrent.shape[0]

    hands,img=detector.findHands(img)
    cv2.line(img,(0,gestureThreshold),(width,gestureThreshold),(0,255,0),10)
    if hands and buttonPressed is False:
        hand=hands[0]
        fingers=detector.fingersUp(hand)
        cx,cy=hand['center']
        lmList=hand['lmList']
        xVal = int(np.interp(lmList[8][0], [width//2, width], [0, width]))
        yVal = int(np.interp(lmList[8][1], [150, height-150], [0, height]))
        indexFinger=xVal,yVal

        # print(fingers)
        
        if cy<=gestureThreshold:    # if the hand at the height of the face

            #Gesture 1 - left
            if fingers==[1,0,0,0,0]:
                print("Left")
                if imgNumber>0:
                    buttonPressed=True
                    imgNumber-=1

            #Gesture 2 - right
            if fingers==[0,0,0,0,1]:
                print("Right")
                if imgNumber<len(pathImages)-1:
                    buttonPressed=True
                    imgNumber+=1
            
        #Gesture 3 - show pointer
        if fingers==[0,1,1,0,0]:
            cv2.circle(imgcurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotations.append(indexFinger)

        if fingers==[0,1,0,0,0]:
            cv2.circle(imgcurrent,indexFinger,12,(0,0,255),cv2.FILLED)

    #Button pressed iterations
    if buttonPressed:
        buttonCounter+=1
        if buttonCounter>buttonDelay:
            buttonCounter=0
            buttonPressed=False

    for i in range (len(annotations)):
        if i!=0:
            cv2.line(imgcurrent,annotations[i-1],annotations[i],(0,0,200),12)


    #Adding webcam image on the slide on the top right corner
    imgsmall =cv2.resize(img,(ws,hs))
    h, w, _=imgcurrent.shape
    imgcurrent[0:hs,w-ws:w]=imgsmall

    cv2.imshow("Image",img)
    cv2.imshow("Slides",imgcurrent)

    key=cv2.waitKey(1)
    if key==ord("q"):
        break
