# 1-45 까지의 숫자를 넣어서 로또 리스트와 입력 리스트 생성
from random import*
lotto = []      # 1 - 45 사이의 랜덤한 숫자 6개
mynum = []      # 1 - 45 사이 입력한 6개 숫자

l = []
for i in range(1,46):
    l.append(i)

for j in range(2000):
    tmp = randint(0,44)
    l[0],l[tmp] = l[tmp], l[0]

for _ in range(1,7):
    lotto.append(l[_])

for k in range(6):
    a = int(input('{}번째 숫자를 입력하세요 >>'.format(k+1)))
    mynum.append(a)

print(lotto)
print(mynum)

ok = []

for t in range(6):
    if mynum[t] in lotto:
        ok.append(mynum[t])
        
print('일치하는 숫자는 {}입니다.'.format(ok))
    
    
    #lotto[t] 번을 mynum의 모든 수와 비교했을 때 같은 수가 있다면
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    