import requests
from bs4 import BeautifulSoup
url = "https://www.gmarket.co.kr/n/best"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
#-------------------------------------------
# num_1 = soup.find('li',{'class':'first'})
# # print(num_1)
# num_2 = num_1.find('p',{'class':'no1'}).text
# print(num_2)

# cont_1 = num_1.find('a',{'class','itemname'}).text
# print(cont_1)

# price_1 = num_1.find('strong')
# price_2 = price_1.find('span').text
# print(price_2)
#-------------------------------------------

# price_1 = num_1.find('span',{'class','for-a11y'}).text
# print(price_1)

#-------------------------------------------
all_1 = soup.find('div',{'class':'best-list'})
# print(allnum_1)

allnum_2 = all_1.find_all('p')
allcont_1 = all_1.find_all('a',{'class','itemname'})
allprice_1 = all_1.find_all('strong')
for i in range(5):
    print(allnum_2[i].text)
    print(allcont_1[i].text)
    print(allprice_1[i].text)
    print('----------------')
    
