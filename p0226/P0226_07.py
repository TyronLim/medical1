#random 함수
# from random import *

# print(random()) #0.0 ~ 1.0 미만의 읨의의 값 생성

# print(int(random()*10))# 0~10 미만의 임의의 값 생성

# print(int(random()*10)+1)     #1~10 이하의 임의의 값 생성

# # 1~45 이하의 임의의 값 생성
# print(int(random()*45)+1)

# print(randrange(1,46)) # 1~46 미만의 임의의 값 생성
# print(randrange(1,46)) # 1~46 미만의 임의의 값 생성
# print(randrange(1,46)) # 1~46 미만의 임의의 값 생성

# print(randint(1,45)) # 1~45 이하의 임의의 값 생성
# print(randint(1,45)) # 1~45 이하의 임의의 값 생성
# print(randint(1,45)) # 1~45 이하의 임의의 값 생성



# 1~10 사이의 숫자를 입력받아서 랜덤한 숫자와 비교해 같으면 [당첨], 다르면 [탈락] 출력

from random import*

a = int(input('숫자를 입력하세요 > '))
b = int(random()*10)+1

if a == b :
    print('당첨')
else :
    print('당첨 숫자는 {}로 일치하지 않습니다.'.format(b))
 
