from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get('http://localhost:8000/lestaches/')
assert 'Taches' in browser.title

time.sleep(3)
browser.quit()
