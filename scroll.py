import cv2
import numpy as np
cap = cv2.VideoCapture(0)
lower_black = np.array([0, 0, 0])
upper_black = np.array([350,55,100])
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_black, upper_black)
    contours, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0,255,0), 2)


    cv2.imshow('Frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

