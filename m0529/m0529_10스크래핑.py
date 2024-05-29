from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

name = []
category = []
content = []
sites = []

url = 'https://namu.wiki/RecentChanges'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(1)
soup = BeautifulSoup(browser.page_source,'lxml')
d_1 = soup.find_all('div',{'class':'b5G6-Ki+'})
# d_1_1 = soup.find_all('div',{'class':'tMX2P1XP'})
# print(d_2)
# # print(d_1)
for i in range(50):
    d_2 = d_1[i+1].find('a')['href']
    sites.append('https://namu.wiki'+d_2)
    url = 'https://namu.wiki'+d_2
    browser.get(url)
    print('https://namu.wiki'+d_2)









# elem = browser.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[5]/article/div[3]/div/div[2]/div[2]/div[1]/a')
# print(elem.text)
# name.append(elem.text)
# elem.click()
# time.sleep(2)
# cate = soup.find('li',{'class':'_5YOCljOj'}).text

# time.sleep(1)
# print(cate)
# print(cont)
# category.append(cate)
# content.append(cont)



# time.sleep(30)


