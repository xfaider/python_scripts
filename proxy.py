from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

def install_proxy(PROXY_HOST, PROXY_PORT):
	fp = webdriver.FirefoxProfile()
	print(PROXY_HOST)
	print(PROXY_PORT)
	fp.set_preference("network.proxy.type", 1)
	fp.set_preference("network.proxy.http", PROXY_HOST)
	fp.set_preference("network.proxy.http_port", int(PROXY_PORT))
	fp.set_preference("network.proxy.https", PROXY_HOST)
	fp.set_preference("network.proxy.https_port", int(PROXY_PORT))
	fp.set_preference("network.proxy.ssl", PROXY_HOST)
	fp.set_preference("network.proxy.ssl_port", int(PROXY_PORT))
	fp.set_preference("network.proxy.ftp", PROXY_HOST)
	fp.set_preference("network.proxy.ftp_port", int(PROXY_PORT))
	fp.set_preference("network.proxy.socks", PROXY_HOST)
	fp.set_preference("network.proxy.socks_port", int(PROXY_PORT))
	fp.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:74.0) Gecko/20100101 Firefox/74.0")
	fp.update_preferences()
	return webdriver.Firefox(firefox_profile=fp)

# 92.41.71.199	3128



browser = install_proxy("62.33.207.196", "3128")
browser.get('https://cryt.crytrex.com/faucetcryt')
#address_field = browser.find_element_by_id('einsatz').send_keys("CRYT-9RHK-MAEJ-VK7H-EVNDW") 
