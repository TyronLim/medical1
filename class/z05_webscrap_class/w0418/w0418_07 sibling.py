import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
type_tr = soup.find("tr",{"class":"type1"})

# print(type_tr.th.find_next_sibling('th'))   # 현재 것에서 다음 형제 것을 찾는다.
# print(type_tr.th.find_previous_sibling('th'))   # 현재 것에서 이전 형제 것을 찾는다.
# print(type_tr.th.find_next_siblings('th'))   # 현재 것에서 다음 형제의 모든 것을 찾는다.
# print(type_tr.th.next)  # th태그 다음단락
# print(type_tr.th.next.next) # </th>
# print(type_tr.th.next.next.next) # 다음 <th>
