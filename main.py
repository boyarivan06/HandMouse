import cv2
import HandTrackingModule as htm
# import cvzone
import numpy as np
import sys
import pyautogui
from PyQt5 import QtWidgets


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = htm.HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)
app = QtWidgets.QApplication(sys.argv)
desktop = QtWidgets.QApplication.desktop()
cx, cy, w, h = 100, 100, desktop.width(), desktop.height()
title = 'Image'

# При подключении камеры могут возникнуть ошибки, поменяйте 0 из cap=cv2.VideoCapture(0) на 1 или 2.

# cx, cy - координаты левой верхней точки нашего четырехугольника
# w, h - ширина и длина (в нашем случае будет квадрат)

stop = False
enabled = True
while not stop:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    res_dec = detector.findHands(img)
    if res_dec.any():
        img = res_dec
    lmList, _ = detector.findPosition(img)
    res = detector.get_finger_coords(4)
    if res:
        pyautogui.moveTo(res[0], res[1])
    if len(lmList) != 0:
        length_click, _, _ = detector.findDistance(8, 4, img, draw=False)
        length_enable, _, _ = detector.findDistance(12, 4, img, draw=False)
        if length_click < 50 and enabled:
            print('CLICK!!!')
            title = 'CLICK'
            pyautogui.click()

        else:
            print('hand detected')
            '''if length_enable < 50:
                        enabled = not enabled
                        print('enabled' if enabled else 'disabled')'''

        # Draw
    '''imgNew = np.zeros_like(img, np.uint8)
    out = img.copy()
    alpha = 0.1
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
'''
    # cv2.imshow(title, out)
    # cv2.waitKey(1)
