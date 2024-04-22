import requests
from bs4 import BeautifulSoup
url = "https://browse.auction.co.kr/list?category=22160000"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",'Accept-Language':"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# with open('auction.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())

# print(soup.prettify())

cnt = 0
# print(len(re2))
for i in range(2,20):
    if cnt==10: break
    s_1 = soup.find_all('div',{'class':'section--itemcard'})
    re = s_1[i].find('ul',{'class':'list--score'})
    re2 = re.find_all('span')
    if len(re2)>2:
        # print(s_1[2])
        brand = s_1[i].find('span',{'class':'text--brand'}).text
        # print(brand)
        name = s_1[i].find('span',{'class':'text--title'}).text
        price = s_1[i].find('strong',{'class':'text__price-seller'}).text
        rank = s_1[i].find('div',{'class':'section--itemcard_info_score'})
        rank2 = rank.find('span',{'class':'for-a11y'}).text
        review = rank.find('span',{'class':'text--reviewcnt'}).text
        img = s_1[i].find(attrs={'class':'image--itemcard'})
        img1 = img['src']
        buycnt = s_1[i].find('span',{'class':'text--buycnt'}).text
        cnt += 1
        # if int(buycnt[4:].replace(',','')) >3:
        print('------------------------------')
        print('이름 :',brand,name)
        print('가격 :',price)
        print('별점 :',rank2)
        print('후기 수:',review)
        print('구매건 수 :',buycnt[3:])
        print('이미지 링크 :',img1)
        print('------------------------------')
        # else :
        #     continue




# s_1 = soup.find_all('div',{'class':'section--itemcard'})
# # print(s_1[2])
# brand = s_1[2].find('span',{'class':'text--brand'}).text
# # print(brand)
# name = s_1[2].find('span',{'class':'text--title'}).text
# price = int(s_1[2].find('strong',{'class':'text__price-seller'}).text.replace(',',''))
# rank = s_1[2].find('div',{'class':'section--itemcard_info_score'})
# rank2 = rank.find('span',{'class':'for-a11y'}).text
# review = rank.find('span',{'class':'text--reviewcnt'}).text
# img = s_1[2].find(attrs={'class':'image--itemcard'})
# img1 = img['src']
# # print(img.attrs)


# print('------------------------------')
# print('이름 :',brand,name)
# print('가격 :','{0:,}'.format(price))
# print('별점 :',rank2)
# print('후기 수:',review)
# print('이미지 링크 :',img1)
# print('------------------------------')
# title = soup.title
# print(title)
# title = soup.find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1asqkxl'})
# rank = s_1.find('span',{'class':'css-9ml4lz'})
# print(title)