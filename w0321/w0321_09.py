import requests
from bs4 import BeautifulSoup

url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%93%B1%EC%B4%8C%EC%A3%BC%EA%B3%B5+%EB%B6%84%EC%96%91'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
res = requests.get(url,headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

s_all = soup.find('ol',{'class':'list_place'})
li_list = s_all.find_all('li')

for i in range(len(li_list)):
    s_joo = li_list[i].find_all('dd',{'class':'f_red'})
    title = li_list[i].find('div',{'class':'wrap_tit'}).a.text.strip()
# print(s_joo)
# s_joo5 = s_all[1]
# s_price = s_joo.find_all('dd')
# print(s_price)
# s_list = s_price('dd',{'class':'f_red'})
    print('이름 :',title)
    print('매매시세 :',s_joo[0].text)
    print('전매시세 :',s_joo[1].text)
    print('-'*50)
# with open('real.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())
    
# print('종료')

