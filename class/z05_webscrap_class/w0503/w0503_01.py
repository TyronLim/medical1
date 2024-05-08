import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import oracledb
# 역대관객순
# 이미지, 제목, 누적관객수, 개봉일
# 이미지 저장
# 2023~2020
# 콘솔창에 출력 후 db에 저장

# daum_movie 테이블
# dno 시퀀스
# title 문자타입(100)
# img 문자타입(100)
# audience 숫자타입(10)
# ddate 날짜타입

conn = oracledb.connect(user='ora_user1',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()

url = "https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
browser.get(url)
time.sleep(1)
soap = BeautifulSoup(browser.page_source,'lxml')

elem1 = browser.find_elements(By.XPATH,'//a[text()="2023"]')
# elem1_1 = elem1.find_elements('li')
elem2 = browser.find_element(By.XPATH,'//*[@id="morColl"]/div/c-container/div[2]/c-carousel/div/ul/li[3]/a')
elem3 = browser.find_element(By.XPATH,'//*[@id="morColl"]/div/c-container/div[2]/c-carousel/div/ul/li[4]/a')
elem4 = browser.find_element(By.XPATH,'//*[@id="morColl"]/div/c-container/div[2]/c-carousel/div/ul/li[5]/a')
el_list = [elem1,elem2,elem3,elem4]

# time.sleep(2)
elem2.click()
# for i in range(4):
    # elem = browser.find_element(By.XPATH,f'//*[@id="morColl"]/div/c-container/div[2]/c-carousel/div/ul/li[3]/a')
    # time.sleep(2)
t_1 = soap.find('ul',{'class':'c-list-basic ty_flow35'})
t_1_1 = soap.find_all('div',{'class':'c-item-content'})
# t_1_2 = soap.find('li')
for j in range(10):
    t_2 = t_1_1[j].find('img')['src']          # 이미지
    t_3 = t_1_1[j].find('strong',{'class':'tit-g clamp-g'}).text     # 제목
    t_4 = t_1_1[j].find('p',{'class':'conts-desc clamp-g'}).text[4:-3].replace(',','')     # 누적 관객수
    t_5 = t_1_1[j].find('span',{'class':'conts-subdesc clamp-g'}).text[:-2]   # 개봉일
    print(t_3.strip())  
    print(t_2.strip())  
    print(int(t_4)*10000)  
    print(t_5.strip())  
    # time.sleep(1)
    sql = f"insert into daum_movie values(dno_seq.nextval,'{t_3.strip()}','{t_2}',{int(t_4)*10000},'{t_5.strip()}')"
    cursor.execute(sql)
        


cursor.execute('commit')
cursor.close()
conn.close()

time.sleep(50)















