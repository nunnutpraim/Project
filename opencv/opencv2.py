import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands(max_num_hands=1, min_detection_confidence=0.75, min_tracking_confidence=0.75)
mpDraw = mp.solutions.drawing_utils

tipIds = [4, 8, 12, 16, 20]

pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            h, w, c = img.shape

            # เก็บจุด landmark ทั้งหมด
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            fingers = []

            # --------------------
            # ตรวจว่ามือเป็นซ้ายหรือขวา
            # --------------------
            wrist_x = lmList[0][1]
            pinky_mcp_x = lmList[17][1]

            is_right_hand = wrist_x < pinky_mcp_x   # ข้อมือซ้ายกว่าก้อย → มือขวา

            # --------------------
            # นิ้วโป้ง (ใช้แกน X)
            # --------------------
            if is_right_hand:  
                fingers.append(1 if lmList[4][1] > lmList[3][1] else 0)
            else:  
                fingers.append(1 if lmList[4][1] < lmList[3][1] else 0)

            # --------------------
            # นิ้วชี้ กลาง นาง ก้อย (ใช้แกน Y)
            # --------------------
            for id in range(1, 5):
                # เทียบปลายนิ้วกับข้อนิ้วล่างลงมา 2 จุด
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1)

            cv2.putText(img, f'Fingers: {totalFingers}', (10, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.8, (255, 0, 255), 5)

            mpDraw.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()