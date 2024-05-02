# 야놀자 홈페이지 이동 > 검색창 클릭 호텔 입력 > 날짜선택(6/5~6/6) 확인 > 호텔 텍스트 엔터키 입력
# 스크롤 이동 반복 
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

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()

url = "https://www.yanolja.com/?utm_source=google_sa&utm_medium=cpc&utm_campaign=20738115572&utm_content=160897187931&utm_term=kwd-327025203539&gad_source=1&gclid=EAIaIQobChMIo-mchMjuhQMVNGwPAh0_OAGuEAAYASAAEgKHcPD_BwE"
browser.get(url)
time.sleep(2)
soup = BeautifulSoup(browser.page_source,'lxml')

elem = browser.find_elements(By.CLASS_NAME,'HomeSearchBar_searchBoxArea__1P61S')
elem[0].click()
time.sleep(1)
# browser.switch_to.window(browser.window_handles[1])
time.sleep(1)

elem = browser.find_element(By.XPATH,'//button[@class="NavFilterButton_container__20Hr2 NavFilterButton_collapse__3JGvV SearchInput_calendarButton__3sNMZ"]')
elem.click()
time.sleep(1)
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[4]')
elem.click()
time.sleep(1)
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[5]')
elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button')
elem.click()
time.sleep(2)
elem = browser.find_element(By.CLASS_NAME,'SearchInput_input__342U2')
elem.send_keys('호텔')
elem.send_keys(Keys.ENTER)
time.sleep(5)

prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이:",prev_height)

# cnt = 0
# while True:
#     if cnt == 5: break
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(1)
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     # if prev_height == curr_height:
#     #     break 

#     # prev_height = curr_height
#     print('현재 높이 :',curr_height)
#     cnt += 1

soup = BeautifulSoup(browser.page_source,'lxml')
for i in range(10):
    t_1 = soup.find_all('div',{'class':'PlaceListItemText_container__fUIgA text-unit'})
    t_2 = t_1[i].find('div',{'class':'PlaceListImage_imageText__2XEMn'})['style']        #이미지
    http = t_2.find('http')
    t_2[http:-3]
    t_3 = t_1[i].find('strong',{'class':'PlaceListTitle_text__2511B'}).text        #제목
    t_4 = t_1[i].find('span',{'class':'PlaceListScore_rating__3Glxf'}).text        #평점
    t_5 = t_1[i].find('span',{'class':'PlaceListScore_reviewInfo__3QSCU'}).text[1:-1]        #평가수
    t_6 = t_1[i].find('span',{'class':'PlacePriceInfoV2_discountPrice__1PuwK'})      #가격
    if t_6 == None:
        t_6 = 0
    else:
        t_6 = int(t_6.text.replace(',',''))
    print(t_2[http:-3])
    print(t_3)
    print(t_4)
    print(t_5)
    print(t_6)

    sql = f"insert into yanolja values(yanolja_seq.nextval,'{t_2[http:-3]}','{t_3}',{float(t_4)},{int(t_5.replace(',',''))},{t_6})"
    cursor.execute(sql)

cursor.execute('commit')
cursor.close()
conn.close()
time.sleep(200)
    