# 성별, 키를 입력받아서 남자일 경우 (m) 172.5 이상이면 [평균이상] 이하면 [평균이하]
# 여자일 경우 (f) 159.6 이상이면 [평균이상] 이하면 [평균이하] 라고 출력하기
# 그 외는 잘못입력하셨습니다 라고 출력
gender = input('성별을 입력하세요 ( m M / f F ) >> ')
height = float(input('키를 입력하세요 >> '))

if gender == "m" or gender == 'M' :
    if height >= 172.5:
        print ('[평균이상]')
    else :
        print ('[평균이하]')
elif gender == 'f' or gender == 'F' :
    if height >= 159.6:
        print ('[평균이상]')
    else :
        print ('[평균이하]')        
else :
    print('[잘못입력하셨습니다.]')