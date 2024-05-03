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

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
browser.get(url)
time.sleep(1)
soap = BeautifulSoup(browser.page_source,'lxml')

# elem = browser.find_element(By.XPATH,'//*[@id="headerSearchKeyword"]')
# elem.send_keys('노트북')
# elem.send_keys(Keys.ENTER)

# elem = browser.find_elements(By.XPATH,'//li[@class="search-product  "]')
# t_1 = soap.find('dl',{'class':'search-product-wrap adjust-spacing  coupon  no-review '})
tt = soap.find('ul',{'id':'productList'})
tt_1 = tt.find_all('dl',{'class':'search-product-wrap'})
# print(len(tt_1))
for i in range(35):
    print(i,'번째')
    t_1 = tt_1[i].find('div',{'class':'name'})                      # 제목
    t_2 = tt_1[i].find('img',{'class':'search-product-wrap-img'})   # 이미지
    t_3 = tt_1[i].find('strong',{'class':'price-value'})            # 가격
    t_4 = tt_1[i].find('em',{'class':'rating'})                     # 평점
    t_5 = tt_1[i].find('span',{'class':'rating-total-count'})       # 평가 수
    print(t_1.text)
    print(t_2['src'])
    if t_3 == None:
        t_3 = 0
        continue
    else:
        print(int(t_3.text.replace(',','')))
        t_3 = int(t_3.text.replace(',',''))
        
    if t_4 == None:
        t_4 = 0
    else:
        print(float(t_4.text))
        t_4 = float(t_4.text)
        
    if t_5 == None:
        t_5 = 0
    else:
        print(int(t_5.text[1:-1]))
        t_5 = int(t_5.text[1:-1])
    print('-'*50)
    sql = f"insert into coupang values(coupang_seq.nextval,'{t_1.text}','{t_2['src']}',{t_3},{t_4},{t_5})"
    cursor.execute(sql)
        
cursor.execute('commit')
cursor.close()
conn.close()

time.sleep(50)















