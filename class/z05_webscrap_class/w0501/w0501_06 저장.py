import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import oracledb
conn = oracledb.connect(user='ora_user1',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()

for j in range(4):
    url = f"https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true&page={j+2}"
    browser.get(url)
    time.sleep(3)

    soup = BeautifulSoup(browser.page_source,'lxml')
    s_1 = soup.find_all('a',{'class':'gc-thumbnail-type-seller-card css-wels0m'})
    # print('<<',j+1,'번째 페이지 >>')
    for i in range(len(s_1)):
        s_2 = s_1[i].find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1asqkxl'})
        s_3 = s_1[i].find('span',{'class':'css-1rzfout'})
        s_4 = s_1[i].find('span',{'class':'css-9ml4lz'})
        s_5 = s_1[i].find('span',{'class':'css-oj6onp'})
        s_5_1 = s_1[i].find('div',{'class':'css-nl3cnv'})
        s_6 = s_5_1.find('img',{'class':'thumbnail-image'})
        s_7 = s_1[i].find('span',{'class':'css-5r5920'})
        
        if s_2 != None :
            title = s_2.text
            print(i+1,'번 호텔 :',title)
        else :
            title = ''
        if s_3 != None :
            region = s_3.text
            print(i+1,'번 장소 :',region)
        else :
            region = ''
        if s_4 != None :
            score = float(s_4.text)
            print(i+1,'번 평점 :',score)
        else : 
            score = 0
        if s_5 != None :
            member = int(s_5.text[:-4].replace(',',''))
            print(i+1,'번 평가수 :',member)
        else : 
            member = 0
        if s_6 != None :
            img = s_6['src']
            print(i+1,'번 이미지 :',img)
        else : 
            img = ''
        if s_7 != None :
            price = int(s_7.text.replace(',',''))
            print(i+1,'번 가격:',price)
        else : 
            price = 0
        print('-'*30)
        time.sleep(1)
# print(len(s_1))

    #DB 저장
        sql = f"insert into yeogi values(yeogi_seq.nextval,'{title}','{region}',{score},{member},'{img}',{price})"
        cursor.execute(sql)

        
cursor.execute('commit')
cursor.close()
conn.close()














# url = 
# with open('yeogi1.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())

# elem = browser.find_elements(By.XPATH,'//*[@id="__next"]/div[1]/main/section/div[2]/a[1]/div/div[2]/div[1]/div/div/div[1]/h3')
# elem1 = browser.find_elements(By.XPATH,'//*[@id="__next"]/div[1]/main/section/div[2]/a[1]/div/div[2]/div[1]/div/div/div[2]/span[1]')
# elem2 = browser.find_elements(By.XPATH,'//*[@id="__next"]/div[1]/main/section/div[2]/a[1]/div/div[2]/div[1]/div/div/div[3]/div/span')
# elem3 = browser.find_elements(By.XPATH,'//*[@id="__next"]/div[1]/main/section/div[2]/a[1]/div/div[2]/div[2]/div/div/div/div[2]/span[1]')
# elem4 = browser.find_elements(By.XPATH,'//*[@id="__next"]/div[1]/main/section/div[2]/a[1]/div/div[1]/div[1]/img')

# print(elem[0].text)
# print(elem1[0].text)
# print(elem2[0].text)
# print(elem3[0].text)
# print(elem4[0])

# url = '/yeogi1.html'

# elem = soup.find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1asqkxl'})
# print(elem[0].text)


# time.sleep(30)





