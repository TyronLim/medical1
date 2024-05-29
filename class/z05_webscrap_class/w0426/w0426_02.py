import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

ran = random.uniform(0,3)
print(ran)

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# # url= "https://www.naver.com"
# url= "https://flight.naver.com/flights/domestic/GMP-CJU-20240514/CJU-GMP-20240515?adult=2&fareType=YC"
# #브라우저 열기
# browser = webdriver.Chrome()
# browser.maximize_window() # 창 최대화
# browser.get(url)

# time.sleep(10)
# # elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="domestic_Flight_sK0eA"]')))    # 최대 30초까지 대기
# # elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="domestic_Flight__sK0eA"]')))
# prev_height = browser.execute_script("return document.body.scrollHeight")
# print("최초 높이:",prev_height)

# while True:
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(1)
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     if prev_height == curr_height:
#         break # 같으면 중단하고 빠져나옴.

#     prev_height = curr_height
#     print('현재 높이 :',curr_height)

# soup = BeautifulSoup(browser.page_source,'lxml')

# flights = soup.find_all('div',{'class':'domestic_Flight__sK0eA'})
# print(len(flights))
# print(flights[0])

# with open('flight.html','w',encoding='utf8') as f:
#     f.write(soup.prttify())
    
    

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

w_list = []
name = []
category = []
content = []

url = 'https://namu.wiki/RecentChanges'
browser = webdriver.Chrome()
browser.get(url)

soup = BeautifulSoup(browser.page_source,'lxml')

site = soup.find_all('div',{'class':'tMX2P1XP'})
a = site.find('a')['href']
print(a)








