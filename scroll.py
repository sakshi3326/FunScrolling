import cv2
import numpy as np
import pyautogui
cap = cv2.VideoCapture(0)
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

prev_y = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)

    contours, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

            if y < prev_y:
                pyautogui.press('space')
            prev_y = y

    cv2.imshow('Frame', frame)


    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

