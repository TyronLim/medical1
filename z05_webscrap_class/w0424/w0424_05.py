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
browser.maximize_window()       # 창 최대화
browser.get(url)

#요소선택, 문자입력, 엔터키 입력, 클릭, 스크롤, 마우스 이동
elem = browser.find_element(By.ID,'query')
elem.send_keys('시가총액')
elem.send_keys(Keys.ENTER)  # 엔터 키 누르기

# 시가총액 더보기 클릭
elem = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div[2]/div[2]/div[1]/div[2]/a')