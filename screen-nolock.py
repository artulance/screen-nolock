import pyautogui
import time

while True:
    pyautogui.press('volumedown')
    time.sleep(100)
    pyautogui.press('volumeup')
    time.sleep(100)