import pyautogui
import time


preX, preY = pyautogui.position()

while True:
	time.sleep(30)
	nowX, nowY = pyautogui.position()
	if preX == nowX and preY == nowY:
		pyautogui.moveRel(3, 3)
		time.sleep(1)
		pyautogui.moveRel(-3, -3)
		print("auto prevent sleep")
	else:
		preX, preY = nowX, nowY
		print("mouse active")
