card = [['spade', 7], ['diamond', 'J'], ['diamond', 5], ['clover', 2], ['clover', 6], 
             ['clover', 'A'], ['diamond', 'K'], ['heart', 3], ['diamond', 9], ['heart', 2], 
             ['clover', 'J'], ['spade', 'J'], ['clover', 10], ['heart', 9], ['clover', 8], 
             ['spade', 9], ['spade', 2], ['diamond', 3], ['spade', 6], ['diamond', 6], 
             ['heart', 6], ['diamond', 'A'], ['spade', 8], ['spade', 4], ['spade','A'], 
             ['spade', 'K'], ['spade', 5], ['heart', 'Q'], ['heart', 'J'], ['clover', 'K'], 
             ['heart', 'A'], ['clover', 3], ['diamond', 7], ['spade', 'Q'], ['heart', 5], 
             ['diamond', 10], ['clover', 5], ['diamond', 'Q'], ['heart', 10], ['heart', 4], 
             ['clover', 4], ['diamond', 4], ['clover', 'Q'], ['spade', 3], ['spade', 10], ['heart', 7], 
             ['clover', 9], ['diamond', 8], ['diamond', 2], ['clover', 7], ['heart', 8], ['heart', 'K']]
import random
card_list = []
shape_list = ['spade','diamond','heart','clover']
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i
num_list[0] = 'A'
num_list[10] = 'J'
num_list[11] = 'Q'
num_list[12] = 'K'

card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list:   # ['spade','diamond','heart','clover']
    for j in range(13):
        card_list[cnt] = {'shape' : i, 'num' : num_list[j]}
        cnt += 1 
        # print(card_list[cnt])

# print(card_list)

# 모양 : spade, 번호 : 1

random.shuffle(card_list)
# print(card_list)

cnt = 0
while True:
    print('1. 카드 1장 뽑기')
    print('2. 카드 5장 뽑기')
    print('0. 종료')
    print('카드가 {}장 남았습니다.'.format(len(card_list)-cnt))
    num = int(input('번호를 선택하세요 >> '))
    if num == 1:
        print('모양 : {} , 번호 : {}'.format(card_list[cnt]['shape'],card_list[cnt]['num']))
        cnt += 1
    
    elif num == 2:
        for i in range(5):
            print('모양 : {} , 번호 : {}'.format(card_list[cnt]['shape'],card_list[cnt]['num']))
            cnt += 1
    
    elif num == 0:
        break
        

