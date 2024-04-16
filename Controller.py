import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8,maxHands=2)
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read from camera")
        break
    
    hand,img = detector.findHands(img)
    lmlist,bboxInfo=detector.findPosition(img)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit when 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()
