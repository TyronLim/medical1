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
url= "https://watcha.com/browse/webtoon"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

time.sleep(1)


pre_heigh = browser.execute_script('return document.body.scrollHeight')
print('처음 높이 : ',pre_heigh)
cnt = 1
while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    post_heigh = browser.execute_script('return document.body.scrollHeight')
    if pre_heigh == post_heigh:
        break
    pre_heigh=post_heigh
    print(cnt,'번 내린 후의 높이: ',post_heigh)
    cnt+=1

soup = BeautifulSoup(browser.page_source,'lxml')
section = soup.find_all('section',{'class':'custom-11ytuur e1134x5i3'})
# print(section[14])
elem = section[14].find('div',{'class':'custom-fzgcwl egf8rrz8'})
# print(elem)
elem1 = elem.find(attr={'class':'custom-13tb7en egf8rrz5'}).img['src']
# print(elem1)
elem2 = elem1.img
# elem = section[14].find_elements(By.CLASS_NAME,'custom-13tb7en egf8rrz5')
# print(elem)
# elem = elem[14].find_elements(By.CLASS_NAME,'custom-13tb7en egf8rrz5').attr
# print(elem[14])



input('enter키 입력 시 종료')
browser.quit()  # 화면 닫기 

