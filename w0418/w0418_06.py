import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

cl_1 = soup.find(attrs={"class":"box_type_l"})
cl_2 = cl_1.find_all("tr")
cl_3 = cl_2[2].find_all("td")
for i in cl_3:
    print(i.text.strip(),end="  ")
    
    # find_next_sibling  >> 현재 것의 다음 형제
    # find_previous_sibling  >> 현재 것의 이전 형제
    
# print(cl_1)
# print(soup.find("tbody"))
# print(cl_2[2].text)
# print(cl_2[2].text.strip())
# print(cl_3)
# print(cl_3)
# for i in cl_3:
#     print(i,end="")
# print()

# c_1 = soup.find('div',{"class":"box_type_l"})
# print(c_1)
# c_2 = c_1.find_all("tr")
# print(c_2[2].text)

