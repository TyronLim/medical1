from random import*
## 1- 10의 숫자만 사용
# 1. 변수선언
lotto = []
mynum = []

# 2. 입력받은 숫자 6개

# 3. 로또 번호 생성하기
l = [1,2,3,4,5,6,7,8,9,10]    # 45 까지
for i in range(50):
    tmp = randint(0,9)   #0번방 - 9번방까지 랜덤한 숫자를 생성     # 44번방까지
    l[0], l[tmp] = l[tmp], l[0]

lotto.append(l[0:6])
print('로또 번호 =', lotto)