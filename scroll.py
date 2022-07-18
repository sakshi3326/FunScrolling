import cv2
import numpy as np
cap = cv2.VideoCapture(0)
lower_black = np.array([0, 0, 0])
upper_black = np.array([350,55,100])
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_black, upper_black)


    cv2.imshow('Frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

