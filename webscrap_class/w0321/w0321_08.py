import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/lastsearch2.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')
s_all = soup.find('div',{'class':'box_type_l'})
tr_list = s_all.find_all('tr')

for i in range(2,15):
    stock = tr_list[i]
    td_list = stock.find_all('td')
    
    # if len(td_list) == 1 : continue
    if i == (5*(i+1)+2) and i == (5*(i+1)+3) and i == (5*(i+1)+4) : continue
    print('순위 : ',td_list[0].text)
    print('종목명 : ',td_list[1].find('a').text)
    print('검색비율  : ',td_list[2].text)
    print('현재가  : ',td_list[3].text)
    print('per  : ',td_list[10].text)
    print('roe  : ',td_list[11].text)
    print('-'*50)
    # print(stock)
        
        
        
        
        
        
        

# samsung = tr_list[2]
# naver = tr_list[3]
# hanhwa = tr_list[4]
# huerim = tr_list[5]
# hlb = tr_list[6]

# # print(len(tr_list))

# for i in td_list:
#     print(td_list[1],td_list[2],td_list[3],td_list[10],td_list[11])



    
    
# print(tr_list)
# print(samsung)
# print(td_list)
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