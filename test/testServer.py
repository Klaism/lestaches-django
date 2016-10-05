from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get('http://localhost:8000/')

time.sleep(1)

assert 'lesTaches' in browser.title

time.sleep(1)

browser.quit()
