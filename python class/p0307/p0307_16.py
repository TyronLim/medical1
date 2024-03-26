import random

# 1차원 배열 25개의 리스트 만들기
list = [0 for i in range(25)]
print(list)

# 0으로 20개, 1로 5개 채우기 
for i in range(5):
    list[i] = 1
print(list)

# 랜덤 섞기
random.shuffle(list)
print(list)

# 5 X 5 2차원 리스트에 넣기
list2 = []          # 만들 2차원 리스트
a = []              # list2에 넣을 1차원 리스트
for i, j in enumerate(list):   # i = 0~24   j = 0,0,0,0,0,1,0,0,.........
    if (i+1)%5 == 0:
        a.append(j)
        list2.append(a)
        a= []                   # a 를 초기화
        
    else :
        a.append(j)
print(list2)

# 두 번째 방법
b = [[0]*5 for i in range(5)]  # 공간 만들어 놓기
for i in range(5):
    for j in range(5):
        b[i][j] = list[5*i+j]
print(b)



# 출력
patch = [["?"]*5 for i in range(5)]
        
print('좌표맞추기 게임')
print('-'*50)
print('',0,1,2,3,4,sep = '\t')
print('-'*50)
print()
for i,j in enumerate(patch):
    print(i,'|',end='\t')
    for k in j:
        print(k, end='\t')
    print()
    print()
print('-'*50)

cnt = 0
cnt_try = 0
while True:
    x = int(input('세로 번호 >> '))
    y = int(input('가로 번호 >> '))
    
    if list2[x][y] == 1:
        patch[x][y] = 'O'
        cnt += 1
    else:
        patch[x][y] = 'X'
        
    print('좌표맞추기 게임')
    print('-'*50)
    print('',0,1,2,3,4,sep = '\t')
    print('-'*50)
    print()
    for i,j in enumerate(patch):
        print(i,'|',end='\t')
        for k in j:
            print(k, end='\t')
        print()
        print()
    print('-'*50)
    cnt_try += 1
    
    if cnt_try == 10:
        print('10번의 기회를 모두 사용하셨습니다.')
        break
    print('{}번째 도전입니다.{}번 남았습니다.'.format(cnt_try,10-cnt_try))
    
    if cnt == 4:
        print('축하합니다. {}개를 맞히셨습니다.'.format(cnt))
        break
    

    # 10번 시도 후 프로그램 종료