
from datetime import datetime
import time
import pyautogui

HOXX_ICON = (707,77)



def start_browser():
	pyautogui.click(22,585)
	pyautogui.PAUSE = 3
	pyautogui.moveTo(58,378)
	pyautogui.PAUSE = 3
	pyautogui.moveTo(270,377)
	pyautogui.PAUSE = 3
	pyautogui.click(270,377)
	time.sleep(75)

def dissconnect():
	pyautogui.click(HOXX_ICON)
	time.sleep(30)
	pyautogui.click(570,474)
	time.sleep(15)

def enter_addres():
	pyautogui.click(186,76)
	time.sleep(2)
	pyautogui.typewrite('https://cryt.crytrex.com/')
	time.sleep(2)
	pyautogui.press('enter')
	time.sleep(30)

def set_vpn():
	pyautogui.click(HOXX_ICON)
	time.sleep(30)
	pyautogui.click(510,404)
	time.sleep(30)



start_browser()
set_vpn()
enter_addres()
time.sleep(30)
dissconnect()

