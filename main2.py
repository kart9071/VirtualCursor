import cv2
import os
from cvzone.HandTrackingModule import HandDetector

width,height=1280,720
folderPath="Presentation"

#Variables
hs,ws=int(120*1),int(213*1)
imgNumber=2

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
    pathfullImage=os.path.join(folderPath,pathImages[imgNumber])
    imgcurrent=cv2.imread(pathfullImage)

    hands,img=detector.findHands(img)

    #Adding webcam image on the slide on the top right corner
    imgsmall =cv2.resize(img,(ws,hs))
    h, w, _=imgcurrent.shape
    imgcurrent[0:hs,w-ws:w]=imgsmall

    cv2.imshow("Image",img)
    cv2.imshow("Slides",imgcurrent)

    key=cv2.waitKey(1)
    if key==ord("q"):
        break
