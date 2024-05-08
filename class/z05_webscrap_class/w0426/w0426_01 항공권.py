import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# url= "https://www.naver.com"
url= "https://flight.naver.com/"
#브라우저 열기
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)
# requests, BeautifulSoup - find,find_all
# selenium - find_element, find_elements
# xpath-By.XPATH, class-By.CLASS_NAME, id-By.ID,name-By.NAME
# XPATH - b[text() = "국내"], b[contains(text(),"국")],
# b[@class="send"], b[@id="send"]
time.sleep(2)
# 출발지 선택
elem = browser.find_element(By.XPATH,'//b[text()="ICN"]')
time.sleep(1)
elem.click()
# 국내 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()
# 김포국제공항 선택
# elem = browser.find_element(By.XPATH,'//i[text()="김포국제공항"]')
time.sleep(1)
elem = browser.find_element(By.XPATH,'//i[contains(text(),"김포국제공항")]')
time.sleep(1)
elem.click()

elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
time.sleep(1)
elem.click()# 도착지 선택

elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()# 국내 선택

elem = browser.find_element(By.XPATH,'//i[contains(text(),"제주")]')
time.sleep(1)
elem.click()# 제주국제공항 선택

elem = browser.find_element(By.XPATH,'//button[text()="가는 날"]')
time.sleep(1)
elem.click()    # 가는 날 클릭

elem = browser.find_elements(By.XPATH,'//b[text()="14"]')
time.sleep(1)
elem[1].click()    # 가는 날짜 클릭

elem = browser.find_elements(By.XPATH,'//b[text()="15"]')
time.sleep(1)
elem[1].click()    # 오는 날짜 클릭

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[3]/button[1]')
time.sleep(1)
elem.click()    # 성인 1명 클릭

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]')
time.sleep(1)
elem.click()    # + 클릭

# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/button')
elem = browser.find_element(By.XPATH,'//span[text()="항공권 검색"]')
time.sleep(1)
elem.click()    # 항공권 검색 클릭(1번 누르면 날짜선택 창이 닫힘)

elem = browser.find_element(By.XPATH,'//span[text()="항공권 검색"]')
time.sleep(1)
elem.click()    # 항공권 검색 클릭(1번 더 눌러야 함.)

time.sleep(7)   # 검색하는데 시간이 걸림
# 대기 명령 함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="domestic_Flight_sK0eA"]')))    # 최대 30초까지 대기

# 화면 스크롤 내리기
# 현재 높이
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이:",prev_height)

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 같으면 중단하고 빠져나옴.

    prev_height = curr_height
    print('현재 높이 :',curr_height)

# 웹 스크래핑으로 정보 가져오기 (항공권 정보)






input('enter키 입력 시 종료')

browser.quit()  # 화면 닫기 
# time.sleep(100)






