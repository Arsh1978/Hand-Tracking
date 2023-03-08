import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.7, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = 1
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,self.mpHands.HAND_CONNECTIONS)

        return img

    def findPositions(self,img, handNo = 0, draw = True):

        lmlist = [] #landmark list
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[handNo]


            for id, lm in enumerate(myhand.landmark):
                # print(id,lm)#prints id and landmark id reams points and each id has corresponding lankmark
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)  # this will convert it into pixels
                #print(id, cx, cy)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx,cy), 7, (255,0,0), cv2.FILLED)

        return lmlist



def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)

        lmlist = detector.findPositions(img)
        if len(lmlist) !=0:

            print(lmlist[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)

        if cv2.waitKey(20) & 0xFF==ord('s'):
            break
        #cv2.waitKey(1)

if __name__ == "__main__":
    main()

