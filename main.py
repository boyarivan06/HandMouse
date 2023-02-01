import cv2
import HandTrackingModule as htm
import cvzone
import numpy as np
import os
from win32api import GetSystemMetrics
import pyautogui


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = htm.HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

cx, cy, w, h = 100, 100, GetSystemMetrics(0), GetSystemMetrics(1)

# При подключении камеры могут возникнуть ошибки, поменяйте 0 из cap=cv2.VideoCapture(0) на 1 или 2.

# cx, cy - координаты левой верхней точки нашего четырехугольника
# w, h - ширина и длина (в нашем случае будет квадрат)

stop = False
while not stop:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)
    res = detector.get_finger_coords(8)
    if res:
        pyautogui.moveTo(res[0], res[1], 0.05)
    if len(lmList) != 0:
        length, _, _ = detector.findDistance(8, 4, img, draw=False)
        if length < 20:
            print('CLICK!!!')
        else:
            print('waiting')

        # Draw
    imgNew = np.zeros_like(img, np.uint8)
    '''for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(imgNew, (cx - w // 2, cy - h // 2), (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
        cvzone.cornerRect(imgNew, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)'''

    out = img.copy()
    alpha = 0.1
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]

    cv2.imshow("Image", out)
    cv2.waitKey(1)

