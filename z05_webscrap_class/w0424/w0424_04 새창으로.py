from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By     # 요소 선택
from selenium.webdriver.common.keys import Keys # 키워드 입력

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "http://www.naver.com"
browser = webdriver.Chrome()
browser.get(url)
elem = browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[6]/a')
elem.click()
# 새 창으로
browser.switch_to.window(browser.window_handles[1])
# url = "https://finance.naver.com/"
# browser = webdriver.Chrome()
# browser.get(url)


elem = browser.find_element(By.XPATH,'//*[@id="container"]/div[2]/div/div[3]/a')
elem.click()

time.sleep(50)





