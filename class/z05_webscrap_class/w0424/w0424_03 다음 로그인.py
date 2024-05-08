from selenium import webdriver
from bs4 import BeautifulSoup
# import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://www.daum.net/"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)

elem = browser.find_element(By.CLASS_NAME,'btn_login')
# elem = browser.find_element(By.XPATH,"")
elem.click()
time.sleep(3)

input_js = 'document.getElementById("loginId--1").value="{id}"; \
            document.getElementById("password--2").value="{pw}";\
            '.format(id="adasdasd",pw="aasd")
browser.execute_script(input_js)
time.sleep(50)

















# elem = browser.find_element(By.ID,'loginId--1')
# # elem = browser.find_element(By.NAME,'loginId')
# elem.send_keys('asdasdsa')
# time.sleep(1)
# elem = browser.find_element(By.ID,'password--2')
# elem.send_keys('asdasdas')
# time.sleep(2)
# elem = browser.find_element(By.CLASS_NAME,'highlight')
# elem.click()
# # time.sleep(5)
# # elem = browser.find_element(By.CLASS_NAME,'recaptcha-checkbox-border')
# # elem.click()

# time.sleep(50)