import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = "https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

l_1 = []    
l_2 = []    
l_3 = []    
l_4 = []
for i in range(5):
    m_1 = 2019+i                                                  # 연도
    url = f"https://search.daum.net/search?w=tot&q={m_1}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source,'lxml')
    # main_window = browser.current_window_handle
    elem = browser.find_elements(By.CLASS_NAME,'wrap_thumb')
    elem[0].click()
    time.sleep(2)
    
    soup = BeautifulSoup(browser.page_source,'lxml')
    # t_1 = soup.find_all('ul',{'class':'c-list-basic ty_flow35'})[0]
    m_2 = soup.find('strong',{'class':'tit-g clamp-g'}).text        # 제목
    m_3 = soup.find('div',{'class':'item-content'})
    m_3_1 = m_3.find_all('dd')                                      # 관객 수
    m_4 = soup.find('c-star',{'class':'_cubic hydrated'})
    m_4_1 = soup.find('span',{'class':'gem-star-point'}).text

    print(m_1)
    print(m_2)
    print(m_3_1[5].text[:-1].replace(',','')) 
    print(m_4_1[2:-8])                                              # 평점
    l_1.append(m_1)  
    l_2.append(m_2)  
    l_3.append(m_3_1[5].text[:-1].replace(',',''))  
    l_4.append(m_4_1[2:-8])  
    
data = {'year':l_1,
        'title':l_2,
        'num':l_3,
        'rating':l_4        
        }

print(data)



time.sleep(30)


