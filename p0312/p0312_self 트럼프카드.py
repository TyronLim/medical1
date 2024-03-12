# import random

# card_list = []
# shape_list = ['spade','diamond','heart','clover']
# num_list = [i for i in range(1,14)]
# num_list[0] = 'A'
# num_list[10] = 'J'
# num_list[11] = 'Q'
# num_list[12] = 'K'
# # print(num_list)

# card_list = [[0,0] for i in range(52)]
# cnt = 0
# for i in shape_list:
#     for j in num_list:
#         card_list[cnt] = [i,j]
#         cnt += 1

# # print(card_list)
# random.shuffle(card_list)
# print(card_list)

# count = 0
# while True :
#     print('카드뽑기')
#     print('1. 1장 뽑기')
#     print('2. 5장 뽑기')
#     print('0. 취소')
#     choice = int(input('번호 선택 >>'))
    
#     if choice == 0:
#         print('취소')
#         break
#     elif choice == 1:
#         print(card_list[count])
#         count += 1
#     elif choice == 2:
#         for i in range(5):
#             print(card_list[count])
#             count+=1


