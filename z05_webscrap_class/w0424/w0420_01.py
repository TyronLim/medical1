from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "http://www.google.com/"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')
with open("google.html",'r',encoding='utf8') as f:
    soup = BeautifulSoup(f,'lxml')                      ## 저장한 파일로 열어버리기

# print('타이틀 : ', soup.title)
# with open('google.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())

