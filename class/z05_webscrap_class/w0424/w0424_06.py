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
browser.maximize_window()
browser.get(url)
elem = browser.find_element(By.ID,'query')
elem.send_keys('네이버 항공권')
elem.send_keys(Keys.ENTER)

elem = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a')
elem.click()

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[1]')
elem.click()
#--------------starting point click






