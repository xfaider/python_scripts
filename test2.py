from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime

start_time = datetime.now().time()
print(start_time)
print("#"*20)
for i in range(5):
	browser = webdriver.Firefox()
	browser.get('https://cryt.crytrex.com/create')
	address = browser.find_element_by_id('address')  
	passwd = browser.find_element_by_class_name('form-control')
	print(address.text)
	print(passwd.get_attribute('value'))
	browser.quit()
finish_time = print(datetime.now().time())


