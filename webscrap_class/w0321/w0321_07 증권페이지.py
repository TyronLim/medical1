import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/lastsearch2.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')
s_all = soup.find('div',{'class':'box_type_l'})
tr_list = s_all.find_all('tr')
# print(tr_list)
samsung = tr_list[2]
# print(samsung)
td_list = samsung.find_all('td')
print(td_list)
# print(samsung.find('a'))
# print('순위 : ',td_list[0].text)
# print('종목명 : ',td_list[1].find('a').text)
# print('검색비율  : ',td_list[2].text)
# print('현재가  : ',td_list[3].text)
# print(len(tr_list))
# print(tr_list[2])

# with open('stock.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())




# s1 = soup.find('a',{'class':'tltle'})
# s2 = soup.find('div',{'class':'box_type_l'})('td',attrs={'class':"no"})
# # s3 = 
# print(s1.text)
# print(s2)
# print(s3.text)





# print(soup.prettify())
