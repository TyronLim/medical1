from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import random
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = 'http://www.naver.com'
browser = webdriver.Chrome()  # 크롬 브라우저 열기
browser.get(url)              # 네이버 페이지로 이동
time.sleep(3)                 # 3초
elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')  #위치로 이동(로그인)
elem.click()                # 위치 클릭
time.sleep(random.randint(2,5))

 # jquery > $("#id"),  javascript > document.getElementById('id').value
# input_js = f'document.getElementById("id").value="{id}"; document.getElementById("pw").value="{pw}";
# input_js = ''.format('aaa','1111')

# 자동화 방지를 위한 자바스크립트 활용 데이터 입력
input_js = 'document.getElementById("id").value="{id}"; \
            document.getElementById("pw").value="{pw}";\
            '.format(id="adasdasd",pw="aasd")
time.sleep(random.randint(2,5))
browser.execute_script(input_js)    # 자바 스크립트 명령어 실행

# elem = browser.find_element(By.ID,'id')    # 아이디 입력창 선택
# time.sleep(random.randint(2,5))
# elem.send_keys('aaa')                      # text 안에 원하는 텍스트 입력
# elem = browser.find_element(By.ID,'pw')
time.sleep(random.randint(2,5))
# elem.send_keys('1111')
elem = browser.find_element(By.CLASS_NAME,'btn_login')
time.sleep(random.randint(2,5))
elem.click()
time.sleep(100)
