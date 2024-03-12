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
print(num_list)
# 카드 1 세트를 생성해보세요

card_list = [[0]*2 for i in range(52)]
cnt = 0
for i in shape_list:   # ['spade','diamond','heart','clover']
    for j in range(13):
        card_list[cnt] = [i,num_list[j]]
        # print(card_list[cnt])
        cnt+= 1
print('-'*50)
# print(card_list)                # 52장의 카드 1 세트
        
random.shuffle(card_list)
print('-'*50)
# print(card_list)                # 52장의 섞인 카드 1 세트

arr_num = 0
while True:
    print('1. 카드 1장 뽑기')
    print('2. 카드 5장 뽑기')
    print('0. 종료')
    print(f'현재 남은 카드는 {len(card_list)-arr_num}장입니다.')
    c_num = int(input('번호를 선택해주세요 >> '))
        
        
    if c_num == 1:
        print(card_list[arr_num])
        arr_num+=1
    elif c_num == 2:
        for i in range(5):
            print(card_list[arr_num])
            arr_num+=1
            














# card = [0,0]
# for i in shape_list:
#     card = []
#     card.append =i
#     for j in num_list:
#         card.append = j
#         print(card) 
#     card_list.append(card)

# print(card_list)
    





