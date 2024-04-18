# 1. 0으로 25개 1차원 리스트 생성
a = [0 for i in range(25)]
print(a)

# 2. 1로 5개를 변경
for i in range(5):
    a[i] = 1
print(a)

# 3. 랜덤섞기
import random
random.shuffle(a)
print(a)

# 4. 5*5 2차원 리스트에 넣기
list = []                 # 만들 2차원 리스트
b = []                    # 2차원 안에 1차원 리스트
for i,j in enumerate(a):
    if (i+1)%5 == 0:
        b.append(j)
        list.append(b)
        b=[]
    else : 
        b.append(j)
print(list)
        
# 추첨 5*5 2차원 배열
print(0,1,2,3,4,sep='\t')
print('-'*60)
for i, j in enumerate(list):
    for k in j:
        print()
        print(k,end='\t')
    print()


# 5. checkList 출력
# 6. viewList 출력
# 7. 좌표입력후 확인
