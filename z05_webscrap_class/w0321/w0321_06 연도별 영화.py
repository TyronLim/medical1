import requests
from bs4 import BeautifulSoup



total = []
total_a = []
for y_i,y in enumerate(range(2021,2024)):
    url = f'https://search.daum.net/search?w=tot&q={y}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
    res = requests.get(url,headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,'lxml')

    movie_list = soup.find('ol',{'class':'movie_list'})

    print('-'*60)
    # 30개
    m_list = movie_list.find_all('li')
    
    print(m_list)

    sum = 0
    for i,m in enumerate(m_list):
        if i == 5: break
        print('번호',i+1)
        print('제목 :',m.find('div',{'class':'info_tit'}).a.text)
        print('평점 :',m.find('em',{'class':'rate'}).text)
        print('-'*70)
        img_screen = m.find('img')['data-original-src']
        print(img_screen)
        # with open(f'movie_{y}_{i}.jpg','wb') as f:
        #     re_img = requests.get(img_screen)       # url 링크를 다시 잃어와야 함.
        #     f.write(re_img.content)     # 파일이름의 내용을 저장
        
        a = float(m.find('em',{'class':'rate'}).text )
        
        sum = sum + a
        
    total.append(f'{sum}')
    total_a.append(float('{:.2f}'.format(sum/5)))    
        
# print('2021 총점의 합 :',total[0])
# print('2022 총점의 합 :',total[1])
# print('2023 총점의 합 :',total[2])

print('총점 합 :',total[0],total[1],total[2])
print('총점 평균 :',total_a[0],total_a[1],total_a[2])
    
print('개수 :',len(m_list))

# print(movie_list)
print('종료')
