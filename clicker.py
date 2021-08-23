import pyautogui
from time import sleep
currentMouseX, currentMouseY = pyautogui.position()

sleep(5)
number = 0
while number < 1000:
 pyautogui.doubleClick()
 number += 1
