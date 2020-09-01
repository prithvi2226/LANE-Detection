import cv2 as cv
import numpy as np


cap = cv.VideoCapture('/Lane.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    #frame = lanesDetection(frame)
    cv.imshow('Lanes Detection', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break