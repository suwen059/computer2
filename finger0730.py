from hand0730 import HandDetector
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.5, maxHands=2)

while True:
    # Get image frame
    success, img = cap.read()

    # Find the hand and its landmarks
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    if lmList:
        bbox = bboxInfo['bbox']
        # Find how many fingers are up
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        cv2.putText(img, f'Fingers:{totalFingers}', (bbox[0] + 200, bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Find Distance Between Two Fingers
        distance, img, info = detector.findDistance(4, 8, img)
        cv2.putText(img, f'Dist:{int(distance)}', (bbox[0] + 400, bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Find Hand Type
        myHandType = detector.handType()
        cv2.putText(img, f'Hand:{myHandType}', (bbox[0], bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    # Display
    cv2.imshow("Image", img)
    k=cv2.waitKey(1)
    if k==27:
        break
cv2.destroyAllWindows()