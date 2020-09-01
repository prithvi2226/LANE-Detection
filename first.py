import cv2
import numpy as np

cap = cv2.VideoCapture('Lane.mp4')

while True:
    success, img = cap.read()
    cv2.imshow("Lane Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break