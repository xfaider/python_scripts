from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time



browser = webdriver.Firefox()
browser.get('https://cryt.crytrex.com/faucetcryt')
address_field = browser.find_element_by_id('einsatz').send_keys("CRYT-RVT4-KDH8-SAGD-CFEMJ") 
#passwd = browser.find_element_by_class_name('form-control')
button_weel = browser.find_element_by_class_name('button')
time.sleep(1)
button_weel.click()