import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=%ED%99%98%EC%9C%A8+1%EB%8B%AC%EB%9F%AC"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

# print(soup)

# with open("google1.html",'w',encoding='utf8') as f:
#     f.write(soup.prettify())

title = soup.find('title')
# print(title.text)

won_1 = soup.find('input',{'class':'lWzCpb ZEB7Fb'})
won_2 = won_1["value"]
print(won_2)

dol_1 = soup.find('input',{'class':'lWzCpb a61j6'})
dol_2 = dol_1["value"]
print(dol_2)
