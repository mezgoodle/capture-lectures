import pyautogui
import cv2
import numpy as np

import time
from datetime import date

today = date.today()
date_format = today.strftime("%d-%m-%Y")

subject_name = 'Economics'

counter = 0

while True:
	time.sleep(2)
	screenshot_name = f'{subject_name}_{date_format}_{counter}.png'
	previous = cv2.imread(screenshot_name)
	if previous is not None:
		current_screen = pyautogui.screenshot()
		current = np.array(current_screen)
		difference = cv2.subtract(previous, current)
		b, g, r = cv2.split(difference)
		if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
			pass
		else:
			counter += 1
			screenshot_name = f'{subject_name}_{date_format}_{counter}.png'
			current_screen.save(screenshot_name)
	else:
		_ = pyautogui.screenshot(screenshot_name)
