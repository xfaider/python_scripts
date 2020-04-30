

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import pyautogui


while True:
	browser = webdriver.Firefox()
	browser.get('https://freebitco.in')
	login_btn = browser.find_element_by_class_name('login_menu_button')
	time.sleep(1)
	login_btn.click()
	email_field = browser.find_element_by_id('login_form_btc_address').send_keys("zclaster@ex.ua")
	passwd_field =  browser.find_element_by_id('login_form_password').send_keys("wJJrTRadBRtykn7i")
	login_btn_press = browser.find_element_by_id('login_button').click()
	time.sleep(15)
	pyautogui.click(405,296)
	time.sleep(5)
	pyautogui.press('end')
	time.sleep(7)

	#try:
	#	pyautogui.click(268,321)
	#	time.sleep(5)
	#	browser.find_element_by_id('free_play_form_button').click()
	#else:

	browser.find_element_by_id('play_without_captcha_container').click()
	time.sleep(5)
	pyautogui.press('end')
	time.sleep(5)
	browser.find_element_by_id('free_play_form_button').click()
	time.sleep(5)
	browser.quit()
	print("OK")
	time.sleep(3600)

