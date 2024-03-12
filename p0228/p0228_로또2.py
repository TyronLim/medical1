from random import*

lotto = []
mynum = []
n = []       # 1부터 45까지 랜덤한 숫자

for i in range(1,46):
    n.append(i)         # 우선 n 에다가 1~45의 숫자를 넣는다.

for i in range(2000):     # n에 있는 랜덤한 숫자 하나를 첫번째(n[0]) 숫자랑 바꾼다.
    tmp = randint(0,44)
    n[0], n[tmp] = n[tmp], n[0]     # 이를 2000번 반복함(많이 할 수록 많이 섞임)

for i in range(6):
    lotto.append(n[i])     # 잘 섞인 n의 숫자 45개 중 앞 6개를 lotto에 넣는다. (lotto는 완성됨)

for i in range(6):
    a = int(input('{}번째 숫자를 입력하시오.(1~45, 총 6개 숫자) >> '.format(i+1)))
    mynum.append(a)         # 숫자 6개를 입력받아 mynum 리스트에 넣는다. (mynum도 완성됨)
    
print(lotto)
print(mynum)
ok = []                  # 일치하는 숫자를 넣을 리스트를 만들어 놓고.

for i in range(len(lotto)):
    if mynum[i] in lotto:
        ok.append(mynum[i])

print('일치하는 숫자는 {}입니다.'.format(ok))



