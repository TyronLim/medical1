card_list = []
shape_list = ['spade','diamond','heart','clover']
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i
num_list[0] = 'A'
num_list[10] = 'J'
num_list[11] = 'Q'
num_list[12] = 'K'

print(shape_list)
print(num_list)
# 2차 리스트로 넣기
card_list = [[0]*2 for i in range(52)]

cnt = 0
print(card_list)
for i in shape_list:
    for j in num_list:    
        card_list[cnt] = [i,j]
        # print(card_list[cnt])
        cnt+= 1

import random
print(card_list)
random.shuffle(card_list)

arr = 0
while True:
    print('1. 카드 1장 뽑기')
    print('2. 카드 5장 뽑기')
    print('0. 종료')
    print(f'현재 남은 카드는 {len(card_list) - arr}장 입니다.')
    put = int(input('번호 선택 >> '))

    if put == 1:
        print(card_list[arr])
        arr+=1
        
    elif put == 2:
        for i in range(5):
            print(card_list[arr])
            arr+=1
            
    elif put == 0:
        print('종료되었습니다.')
        break




