import mediapipe as mp
import cv2
import time


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpdraw = mp.solutions.drawing_utils#draw lines on hand

#for fps
Ctime = 0
ptime = 0
#video capture

cap = cv2.VideoCapture(0)
while(True):
    success, img = cap.read()

    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)# because mediapipe follows rgb
    results = hands.process(imgrgb)#process the results
    #  print(results.multi_hand_landmarks)  #returns none if no hands detected else return coordinated

    if results.multi_hand_landmarks: #if hand detected for each hand draw lines
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                #print(id,lm)#prints id and landmark id reams points and each id has corresponding lankmark
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)#this will convert it into pixels
                print(id,cx,cy)
            mpdraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)

    ctime =time.time() #calculating FPS
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img, str(fps),(10,70),cv2.FONT_HERSHEY_SIMPLEX, 2 , (179,253,253), 2)#givnig colour size to fps and can also be converted into integer

    cv2.imshow('Image',img)

    if cv2.waitKey(1) & 0xFF == ord('f'):
        break

cap.release()
cv2.destroyAllWindows()
