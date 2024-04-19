import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

s_1 = soup.find('div',{"class":"box_type_l"})
# # print(s_1)
s_2 = s_1.find_all('tr')
# # print(s_2)
# s_3 = s_2.find_next_sibling('tr')
# # print(s_3)
# s_4 = s_3.find_next_siblings('tr')
# print(s_4)

for i in range(2,16):
    s_3 = s_2[i].find_all('td')
    if len(s_3)!=1:
        for j in range(12):
            print(s_3[j].text.strip(),end=" ")
        print()

# s_3 = 
# print(s_2)
# s_3 = s_2[2].find_all("td")
# for i in s_2:
#     s_3 = i.find_all("td")
#     if len(s_3)>6:
#         for j in range(len(s_2)):
#             print(s_3[j].txt)
# for k in j
#     print()

# for i in s_2:
#     s_3 = s_2[i]
#     if len(s_3.find_all('td'))>2:
#         print(s_3)
# s_3 = s_2.find_all('td')
# print(s_3)
# for i in s_2:
#     s_2[i].find_all('td')
#     if len(s_3)>3:
#         for j in s_3:
#             print(j.text.strip())







