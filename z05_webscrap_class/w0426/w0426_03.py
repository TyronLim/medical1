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


with open('flight.html','r',encoding='utf8') as f:
    soup = BeautifulSoup(f,'lxml')

flights = soup.find_all('div',{'class':'domestic_Flight__sK0eA'})
print('개수 :',len(flights))
print('-'*50)

for i in range(287):
    airline_name = flights[i].find("b",{"class":"airline_name__Tm2wJ"})
    route_times = flights[i].find_all("b",{"class":"route_time__-2Z1T"})
    air_price = flights[i].find("i",{"class":"domestic_num__2roTW"})
    if int(air_price.text.strip().replace(',','')) > 100000:
        print(i+1,'번째')
        print('-----10만원 이상인 항공권입니다.------')
        print('-'*50)
        continue
    else:
        print(i+1,'번째')
        print('항공사 :',airline_name.text.strip())
        print('출발시간 :',route_times[0].text.strip())
        print('도착시간 :',route_times[1].text.strip())
        print('가격 :',air_price.text.strip())
        print('-'*50)