from random import*

# random = # 0.0~1.0    () 필수
# print(random())

# n1 = randrange(1,10)    #1-9 정수 (10 미만)
# n2 = randrange(10)      #0-10 사이의 정수
# n3 = randint(1,10)      #1-10 사이의 정수

# print(n1,n2,n3)

lotto = []
# lotto에 1-10 사이의 랜덤한 숫자 6개를 넣어보세요
for i in range(6):
    rand = randint(1,10)
    lotto.append(rand)    

mynum = []
# 내가 직접 입력한 숫자 6개를 넣어보세요
for i in range(6):
    var = int(input('숫자를 쓰세요 >> '))
    mynum.append(var)
print(lotto)
print(mynum)

for i in lotto:
    print(i)
    
for i in range(len(lotto)):
    print(lotto[i])