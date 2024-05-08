import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import oracledb

conn = oracledb.connect(user='ora_user1',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

# url = "https://flight.naver.com/"
# browser.get(url)
# time.sleep(1)
# soap = BeautifulSoup(browser.page_source,'lxml')

# elem = browser.find_element(By.XPATH,'//b[text()="ICN"]')
# time.sleep(1)
# elem.click()
# elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
# time.sleep(1)
# elem.click()
# elem = browser.find_element(By.XPATH,'//i[text()="GMP"]')
# time.sleep(1)
# elem.click()
# elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
# time.sleep(1)
# elem.click()
# elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
# time.sleep(1)
# elem.click()
# elem = browser.find_element(By.XPATH,'//i[text()="제주"]')
# time.sleep(1)
# elem.click()
# elem = browser.find_element(By.XPATH,'//button[text()="가는 날"]')
# time.sleep(1)
# elem.click()
# elem = browser.find_elements(By.XPATH,'//b[text()="26"]')
# time.sleep(1)
# elem[1].click()
# elem = browser.find_elements(By.XPATH,'//b[text()="27"]')
# time.sleep(1)
# elem[1].click()
# elem = browser.find_element(By.XPATH,'//button[text()="성인"]')
# time.sleep(1)
# elem.click()
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]')
# time.sleep(1)
# elem.click()
# elem = browser.find_element(By.XPATH,'//span[text()="항공권 검색"]')
# time.sleep(1)
# elem.click()
# elem.click()


url = "https://flight.naver.com/flights/domestic/GMP-CJU-20240626/CJU-GMP-20240627?adult=2&fareType=YC"
browser.get(url)
time.sleep(15)
soap = BeautifulSoup(browser.page_source,'lxml')
# t_1 = soap.find('div',{'class':'domestic_inner__15-bD'})
elem = browser.find_elements(By.XPATH,'//div[@class="domestic_Flight__sK0eA"]')
for i in range(len(elem)):
    elem_1 = browser.find_elements(By.XPATH,'//b[@class="airline_name__Tm2wJ"]')        # 항공사
    print(elem_1[i].text)
    elem_2 = browser.find_elements(By.XPATH,'//b[@class="route_time__-2Z1T"]')        # 가는 시간
    print("6/26:",elem_2[i*2].text)
    print("6/27:",elem_2[i*2+1].text)                                                               # 오는 시간
    elem_3 = browser.find_elements(By.XPATH,'//i[@class="route_info__1RhUH"]')        
    print(elem_3[i].text)                                                               # 소요 시간
    elem_4 = browser.find_elements(By.XPATH,'//i[@class="domestic_num__2roTW"]')        # 가격
    print(elem_4[i].text)       
    sql = f"insert into coupang values\
        (coupang_seq.nextval,'{elem_1[i].text}','{elem_2[i*2].text}',\
            '{elem_2[i*2+1].text}','{elem_3[i].text}',{int(elem_4[i].text.replace(',',''))})"
    cursor.execute(sql)                                                        
# t_1 = soap.find('div',{'class':'domestic_inner__15-bD'})
        
cursor.execute('commit')
cursor.close()
conn.close()

time.sleep(50)















