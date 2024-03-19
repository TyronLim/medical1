import random
# from random import *              >> random 모듈명을 만 붙여도 됨.

print(random.random())                 # 0.000000  ~ 0.9999999999 랜덤 소수점 결과값 출력
print(random.uniform(10,20))           # 10 ~ 20 사이의 랜덤 float 결과값 출력
print(random.randrange(3))             # 0이상 2미만 사이의 랜덤 정수값 출력
print(random.randint(1,10))            # 1이상 10이하 사이의 랜덤 정수값 출력

print(random.choice([1,2,3,4,5]))      # 리스트 내 랜덤 출력

a_list = [1,2,3,4,5]
random.shuffle(a_list)                 # 리스트 섞어서 저장(파괴)
print(a_list)

print(random.choice([1,2,3,4,5]))      # 리스트 내 랜덤 1개 선택
print(random.sample([1,2,3,4,5],k=3))  # 리스트 내 랜덤 3개 선택  sample.     k = 리스트 내 요소보다 클 경우 에러







# import math

# print(math.sin(30))
# print(math.cos(40))
# print(math.tan(45))


