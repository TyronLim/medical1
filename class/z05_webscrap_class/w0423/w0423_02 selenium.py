from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

### selenium 정보 가져오기
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.get("https://comic.naver.com/bestChallenge")
time.sleep(3)
soup = BeautifulSoup(browser.page_source,'lxml')

# with open('webtoons2.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())
# print('완료')

ul_1 = soup.find('ul',{'class':'AsideList__content_list--FXDvm AsideList__challenge--HeKuU'})
# print(ul_1)
li_1 = ul_1.find_all('li',{'class':'AsideList__item--i30ly'})
# print(li_1[0])

for i in range(10):
    no = li_1[i].find('strong',{'class':'AsideList__ranking--sNPZy'}).text
    text = li_1[i].find('span',{'class':'text'}).text
    writer = li_1[i].find('a',{'class':'ContentAuthor__author--CTAAP'}).text
    img = li_1[i].find(attrs={'class':'Poster__image--d9XTI'})['src']
    print('이미지 :',img)
    print('번호 : ',no)
    print('제목 : ',text)
    print('작가 : ',writer)
    img_poster = requests.get(img, headers=headers)
    # with open('weptoons_{}.jpeg'.format(i+1),'wb') as f:
        # f.write(img_poster.content)
    print('-----------')










### requests 정보 가져오기
# url="https://comic.naver.com/bestChallenge"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,'lxml')
# print(soup.prettify())

# with open('webtoons1.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())
# print('완료')

# elem = browser.find_element("MyView-module__link_login___HpHMW")
# elem
# elem.click()