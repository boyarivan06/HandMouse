import cv2
import HandTrackingModule as htm
import pyautogui

CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720

cap = cv2.VideoCapture(0)
cap.set(3, CAMERA_WIDTH)
cap.set(4, CAMERA_HEIGHT)
detector = htm.HandDetector(detectionCon=0.8)

screen_width, screen_height = pyautogui.size()

# При подключении камеры могут возникнуть ошибки, поменяйте 0 из cap=cv2.VideoCapture(0) на 1 или 2.

stop = False
enabled = True
while not stop:
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)
    res_dec = detector.findHands(img)
    if res_dec is not None:
        img = res_dec

    lmList, _ = detector.findPosition(img)
    res = detector.get_finger_coords(4)
    if res:
        mapped_x = int(res[0] * screen_width / CAMERA_WIDTH)
        mapped_y = int(res[1] * screen_height / CAMERA_HEIGHT)
        pyautogui.moveTo(mapped_x, mapped_y)

    if len(lmList) != 0:
        length_click, _, _ = detector.findDistance(8, 4, img, draw=False)
        length_right_click, _, _ = detector.findDistance(4, 12, img, draw=False)
        length_stop, _, _ = detector.findDistance(20, 4, img, draw=False)

        if length_stop < 20:
            stop = True
            print('STOP')
        elif length_click < 60 and enabled:
            print('mouse down')
            pyautogui.mouseDown()
        elif length_right_click < 50 and enabled:
            print('mouse right click')
            pyautogui.click(button='right')
        else:
            pyautogui.mouseUp()
            print('hand detected')
