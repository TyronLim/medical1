
a, b = 10, 8
a, b = b, a

n1 = [0,1,2,3,4,5]
#     0     3     의 위치를 바꾸고 싶다.
n1[0], n1[3] = n1[3], n1[0]
n1[2], n1[5] = n1[5], n1[2]

print(n1)

con =['미국','영국','일본','중국','스페인']

con[1], con[-2] = con[-2], con[1]
print(con)

from random import*
n1 = [1,2,3,4,5,6,7,8,9,10] # 랜덤하게 섞어보자!
for i in range(100):
    tmp = randint(0,9)   # 랜덤한 인덱스 만들기
    n1[0], n1[tmp] = n1[tmp], n1[0]  # 숫자를 서로 바꿔주기
    print(tmp)
    print(n1)