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

conn = oracledb.connect(user='ora_user1',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()

# cursor.fetchall()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()

url = "https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(2)

soup = BeautifulSoup(browser.page_source,'lxml')
m = soup.find('tbody')
m_1 = m.find_all('tr',{'class':'lst50'})
m_1_1 = m.find_all('tr',{'class':'lst100'})


# m_2 = m_1_1[29].find('span',{'class':'rank'}).text     # 순위
# m_3 = m_1_1[29].find('span',{'class':'rank_wrap'}).text   # 변동
# if m_3[4] == '동':
#     m_3 = 0
    
# elif m_3[4] == '상':
#     m_3 = int(m_3[6:].strip())
# else :
#     m_3 = int('-'+m_3[6:].strip())
    
# m_4 = m_1_1[29].find('img')['src']     # 이미지
# m_5div = m_1_1[29].find('div',{'class','ellipsis rank01'}) 
# m_5 = m_5div.find('a').text     # 제목
# m_6div = m_1_1[29].find('div',{'class','ellipsis rank02'})
# m_6 = m_6div.find('a').text     # 가수
# m_7 = m_1_1[29].find('span',{'class':'cnt'}).text[4:]  # 좋아요 수
# print('곡 정보')
# print(m_2)
# print(m_3)
# print(m_4)
# print(m_5)
# print(m_6)
# print(int(m_7.replace(',','')))
# print('-'*50)



# for i in range(len(m_1)):
#     m_2 = m_1[i].find('span',{'class':'rank'}).text     # 순위
#     m_3 = m_1[i].find('span',{'class':'rank_wrap'}).text   # 변동
#     if m_3[-2] == '동':
#         m_3 = 0
        
#     elif m_3[-2] == '상':
#         m_3 = int(m_3[6:].strip())
    # elif m_3[-2] == '진':
    #         m_3 = 0
#     else :
#         m_3 = int('-'+m_3[6:].strip())
        
#     m_4 = m_1[i].find('img')['src']     # 이미지
#     m_5div = m_1[i].find('div',{'class','ellipsis rank01'}) 
#     m_5 = m_5div.find('a').text     # 제목
#     m_6div = m_1[i].find('div',{'class','ellipsis rank02'})
#     m_6 = m_6div.find('a').text     # 가수
#     m_7 = m_1[i].find('span',{'class':'cnt'}).text[4:]  # 좋아요 수
#     print('1위 곡 정보')
#     print(m_2)
#     print(m_3)
#     print(m_4)
#     print(m_5)
#     print(m_6)
#     print(int(m_7.replace(',','')))
#     print('-'*50)

#     sql = f"insert into melon values(melon_seq.nextval, {int(m_2)},{m_3},'{m_4}','{m_5}','{m_6}',{int(m_7.replace(',',''))})"
#     cursor.execute(sql)



for i in range(len(m_1)):
    m_2 = m_1_1[i].find('span',{'class':'rank'}).text     # 순위
    m_3 = m_1_1[i].find('span',{'class':'rank_wrap'}).text   # 변동
    if m_3[-2] == '동':
        m_3 = int(m_3[6:].strip())
        
    elif m_3[-2] == '상':
        m_3 = int(m_3[6:].strip())
    elif m_3[-2] == '진':
        m_3 = 0
    else :
        m_3 = int('-'+m_3[6:].strip())
        
    m_4 = m_1_1[i].find('img')['src']     # 이미지
    m_5div = m_1_1[i].find('div',{'class','ellipsis rank01'}) 
    m_5 = m_5div.find('a').text     # 제목
    m_6div = m_1_1[i].find('div',{'class','ellipsis rank02'})
    m_6 = m_6div.find('a').text     # 가수
    m_7 = m_1_1[i].find('span',{'class':'cnt'}).text[4:]  # 좋아요 수
    print('순번 : ',i)
    print(m_2)
    print(m_3)
    print(m_4)
    print(m_5)
    print(m_6)
    print(int(m_7.replace(',','')))
    print('-'*50)

    sql = f"insert into melon values(melon_seq.nextval, {int(m_2)},{m_3},'{m_4}','{m_5.replace("'","")}','{m_6}',{int(m_7.replace(',',''))})"
    cursor.execute(sql)

cursor.execute('commit')
cursor.close()
conn.close()


