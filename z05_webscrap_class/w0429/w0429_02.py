import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "https://flight.naver.com/"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

time.sleep(1)
elem = browser.find_element(By.XPATH,'//b[text()="ICN"]')   # 인천 클릭
time.sleep(1)
elem.click()
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')   # 국내 클릭
time.sleep(1)
elem.click()    
elem = browser.find_element(By.XPATH,'//i[text()="김포국제공항"]')  # 김포 국제공항 클릭
time.sleep(1)
elem.click()    

#-- 도착지
time.sleep(1)
elem = browser.find_element(By.XPATH,'//b[text()="도착"]')   # 인천 클릭
time.sleep(1)
elem.click()
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')   # 국내 클릭
time.sleep(1)
elem.click()    
elem = browser.find_element(By.XPATH,'//i[text()="제주국제공항"]')  # 김포 국제공항 클릭
time.sleep(1)
elem.click()

elem = browser.find_element(By.XPATH,'//button[text()="가는 날"]') # 가는 날 클릭
elem.click()
time.sleep(1)

elem = browser.find_elements(By.XPATH,'//b[text()="14"]')   # 가는 날짜 클릭
# print(len(elem))
time.sleep(1)
elem[1].click()

elem = browser.find_element(By.XPATH,'//button[text()="오는 날"]') # 오는 날 클릭
elem.click()
time.sleep(1)

elem = browser.find_elements(By.XPATH,'//b[text()="15"]')   # 오는 날짜 클릭
# print(len(elem))
time.sleep(1)
elem[1].click()

elem = browser.find_element(By.XPATH,'//button[contains(text(),"성인")]')
time.sleep(1)
elem.click()

elem = browser.find_elements(By.CLASS_NAME,'searchBox_outer__9n6IB')
time.sleep(1)
elem[0].click()

elem = browser.find_element(By.XPATH,'//span[text()="항공권 검색"]')
time.sleep(1)
elem.click()
elem.click()

# elem = browser.find_element(By.XPATH,'//i[contains(text(),"김포국제공항")]') # 글자 포함검색
# elem = browser.find_elements(By.XPATH,'//b[text()="15') # 여러개
# '//i[@id="_next"]'    # id로
# '//i[@class="_next"]' # class로

# 화면 대기 시간 함수
elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="domestic_Flight__sK0eA"]')))

print(elem)
print(elem[0].text)

prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이:",prev_height)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # 스크롤 높이 체크
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break   
     
    prev_height = curr_height
    print('현재 높이 :',curr_height)
soup = BeautifulSoup(browser.page_source,'lxml')
with open('flight.html','w',encoding='utf8') as f:
    f.write(soup.prettify())
    

    
input('엔터키 입력 시 종료')
browser.quit()







time.sleep(100)

























