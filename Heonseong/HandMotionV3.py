##오른손 왼손 구별 (한 손만) +  관절 구별 (출력 없음) ##

import cv2
from cvzone.HandTrackingModule import HandDetector

# IP WebCam 어플을 사용 할 경우
# cap = cv2.VideoCapture("http://Your IP Number/video")
# WebCam 을 사용할 경우
cap = cv2.VideoCapture(0)


# 손을 감지
detector = HandDetector(maxHands=1, detectionCon=0.8)

while True:
  # 웹켐에서 프레임 가져오기
  success, img = cap.read()

  # Hands
  hands, img = detector.findHands(img)

  cv2.imshow("Image", img)

  if cv2.waitKey(1) == ord("q"): # q 누를 시 웹켐 종료
    break