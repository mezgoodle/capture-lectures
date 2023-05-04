import time
from datetime import date

import cv2
import numpy as np
import pyautogui

TODAY = date.today()
DATE_FORMAT = TODAY.strftime("%d-%m-%Y")
REGION = (241, 52, 1678-241, 1011-52)
SLEEP_SECONDS = 5
SUBJECT_NAME = 'ML'
counter = 46

while True:
	time.sleep(SLEEP_SECONDS)
	screenshot_name = f'{SUBJECT_NAME}_{DATE_FORMAT}_{counter}.png'
	previous = cv2.imread(screenshot_name)
	if previous is not None:
		current_screen = pyautogui.screenshot(region=REGION)
		current = cv2.cvtColor(np.array(current_screen), cv2.COLOR_RGB2BGR)
		difference = cv2.subtract(previous, current)
		b, g, r = cv2.split(difference)
		if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
			print('Skipped')
		else:
			print(cv2.countNonZero(b), cv2.countNonZero(g), cv2.countNonZero(r))
			counter += 1
			print('New photo')
			screenshot_name = f'{SUBJECT_NAME}_{DATE_FORMAT}_{counter}.png'
			current_screen.save(screenshot_name)
	else:
		print('The first photo')
		_ = pyautogui.screenshot(screenshot_name, region=REGION)
