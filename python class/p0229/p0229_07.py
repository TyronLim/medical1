from random import*
# 1-100 사이 랜덤한 숫자를 만들어서 
# 내가 입력한 값이 랜덤한 숫자랑 같으면 당첨(프로그램 종료),아니면 다시 입력해주세요
# 를 출력하는 프로그램을 만들어보세요

# 입력한 숫자가 랜덤 숫자보다 작으면 작습니다.
# 랜덤 숫자보다 크면 더 작은 수를 입력하세요.
# while True:
#     a = int(input('1-100까지의 숫자를 입력하세요>> '))
#     if a == b :
#         print('당첨! 프로그램이 종료됩니다.')
#         break
#     elif a != b :
#         if a < b :
#             print('더 큰 수를 입력해주세요.')
#         elif a > b :
#             print('더 작은 수를 입력해주세요.')
#         print()

# for i in range(100):
#     a = int(input('1-100까지의 숫자를 입력하세요>> '))
#     if a != b :
#         if a>b :
#             print('더 작은 수를 입력하세요.')
#         elif a<b:
#             print('더 큰 수를 입력하세요')
#     elif a == b:
#         print('당첨입니다! 프로그램이 종료됩니다.')
#         break

b = randint(1,100)
# 1. 현재 입력한 숫자 모두를 inputlist에 넣으세요
# inputlist=[]
# while True:
#     num = int(input('숫자를 입력하세요 > '))
#     inputlist.append(num)
#     if num == b:
#         print('당첨!')
#         break
#     elif num < b:
#         print('더 큰 수를 입력하세요')
#     elif num > b:
#         print('더 작은 수를 입력하세요')
    
# print(inputlist)

# 2. 10회 도전 후 프로그램이 종료가 되게 해주세요.
i = 0
while i < 10:
    num = int(input('숫자를 입력하세요>> '))
    if num == b:
        print('당첨!')
        break
    elif num < b:
        print('더 큰 수를 입력하세요')
    elif num > b:
        print('더 작은 수를 입력하세요')
    i += 1

if i ==10 :
    print('10번의 기회를 모두 소진했습니다. 랜덤 숫자는 {}였습니다.'.format(b))

