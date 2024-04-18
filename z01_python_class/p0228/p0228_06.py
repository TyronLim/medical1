from random import*

n1 = randrange(1,11)  # 1-10 사이의 정수
n2 = randint(1,10)    # 1-10 까지의 정수

# 랜덤한 숫자 6개 lotto 리스트에 넣고, 내가 입력한 숫자 6개는 mynum 리스트에 넣기
lotto = []
mynum = []

for i in range(6):
    b = randint(1,10)
    if b not in lotto:
        lotto.append(randrange(6))
# 중복 없이 숫자를 입력(랜덤에서)
for j in range(1,7):
    a = int(input('{}번째 숫자를 입력하세요  >>'.format(j)))
    mynum.append(a)

print(lotto)
print(mynum)