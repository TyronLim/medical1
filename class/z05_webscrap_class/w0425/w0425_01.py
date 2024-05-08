from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By     # 요소 선택
from selenium.webdriver.common.keys import Keys # 키워드 입력

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "https://www.naver.com"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

elem = browser.find_element(By.ID,'query')
elem.send_keys('네이버 항공권')
elem.send_keys(Keys.ENTER)
time.sleep(2)

elem = browser.find_element(By.CLASS_NAME,'link_name')
elem.click()

# 네이버 항공권 창으로 이동
browser.switch_to.window(browser.window_handles[1])

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[1]')
elem.click()
time.sleep(2)
elem = browser.find_element(By.CLASS_NAME,'autocomplete_Collapse__tP3pM')
elem.click()
time.sleep(2)
elem = browser.find_element(By.CLASS_NAME,'autocomplete_Airport__3_dRP')
elem.click()
time.sleep(3)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[2]')
elem.click()
time.sleep(2)
elem = browser.find_element(By.CLASS_NAME,'autocomplete_Collapse__tP3pM')
elem.click()
time.sleep(2)
elem = browser.find_elements(By.CLASS_NAME,'autocomplete_Airport__3_dRP')[1]
elem.click()
time.sleep(2)
# 출발 도착 끝

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[2]/button[1]')
elem.click()
time.sleep(2)

#--- 여기서부터 안 됨
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[11]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[3]/td[3]/button/b')
elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[11]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[3]/td[5]/button/b')
elem.click()
time.sleep(2)






elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[3]/button')
elem.click()
time.sleep(2)

browser.switch_to.window(browser.window_handles[1])
elem = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a')
elem.click()
browser.switch_to.window(browser.window_handles[1])
elem = browser.find_elements(By.CLASS_NAME,'searchBox_outer__9n6IB')[0]
elem.click()

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[1]')
elem.click()
time.sleep(100)




