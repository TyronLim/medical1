from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# selenium은 자동화프로그램
## browser = webdriver.Chrome()
url = "https://news.naver.com/main/ranking/popularDay.naver"
## browser.get(url)
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# 브라우저 페이지 열기
res = requests.get(url,headers=headers)
res.raise_for_status()

## soup = BeautifulSoup(browser.page_source,'lxml')
soup = BeautifulSoup(res.text,'lxml')

ul = soup.find_all('ul',{'class':'rankingnews_list'})
# print(ul[0])

# print(li)
for i in range(12):
    li = ul[i].find_all('li')
    no = li[0].find('em',{'class':'list_ranking_num'}).text
    title = li[0].find('a',{'class':"list_title nclicks('RBP.rnknws')"}).text
    img = li[0].find(attrs={'class':"list_img nclicks('RBP.rnknws')"}).img['src']
    print('번호 : ',no)
    print('제목 : ',title)
    print('이미지 : ',img)
    print('-'*40)
    
