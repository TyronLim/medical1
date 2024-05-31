from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = 'https://www.coupang.com/vp/products/227331483?itemId=720227345&vendorItemId=4822351124&pickType=COU_PICK&q=%ED%95%98%EB%A6%BC+%EB%8B%AD%EA%B0%80%EC%8A%B4%EC%82%B4+%EB%83%89%EB%8F%99&itemsCount=36&searchId=bba132a29f73455ebfc6c74974a229fc&rank=1&isAddedCart='

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(options=options)
browser.get(url)

prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이:",prev_height)

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 같으면 중단하고 빠져나옴.

    prev_height = curr_height
    print('현재 높이 :',curr_height)