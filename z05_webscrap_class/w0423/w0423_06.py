from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
# 서울, 인청, 경기도 인구

# 서울특별시 : 인구
# 인천광역시 : 인구
# 경기도 : 인구
# 합계 : 인구

## browser = webdriver.Chrome()
url = "https://jumin.mois.go.kr/ageStatMonth.do"
## browser.get(url)
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')
# table = soup.find('table',{'id':'contextTable'})
# # print(table)
# body = table.tbody
# # print(body)
# tr = body.find_all('tr')
# # print(tr[1])
# s_td = tr[1].find('td',{'class':'td_admin th1'}).text
# s_td1 = tr[1].find('td',{'title':'2024년 03월 / 계'}).text
# i_td = tr[4].find('td',{'class':'td_admin th1'}).text
# i_td1 = tr[4].find('td',{'title':'2024년 03월 / 계'}).text
# k_td = tr[9].find('td',{'class':'td_admin th1'}).text
# k_td1 = tr[9].find('td',{'title':'2024년 03월 / 계'}).text
# tot = int(s_td1.replace(',','')) + int(i_td1.replace(',','')) + int(k_td1.replace(',',''))
# total = str(tot)[0:2]+','+str(tot)[2:5]+','+str(tot)[5:8]
# print(s_td, ':',s_td1)
# print(i_td, ':',i_td1)
# print(k_td, ':',k_td1)
# print('합계 : ',total)
# # print(td[0])

browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)

s_name = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[2]/td[2]')
s_num = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[2]/td[3]')
i_name = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[5]/td[2]')
i_num = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[5]/td[3]')
k_name = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[10]/td[2]')
k_num = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[10]/td[3]')
print(s_name.text , ':', s_num.text)
print(i_name.text , ':', i_num.text)
print(k_name.text , ':', k_num.text)