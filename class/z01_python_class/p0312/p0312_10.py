import random

# 카드 종류 : SPADE, DIAMOND, HEART, CLOVER
# 카드 숫자 : A,2,3,4,5,6,7,8,9,10,J,Q,K   13장
# 카드 총 수 : 52장

def card_creat():
    chk = 0
    for i in card_shape:
        for j in card_num:
            card_shake[chk] = [i,j]
            chk += 1
    print(card_shake)

def card_shuffle():
    random.shuffle(card_shake)
    print(card_shake)

def card_share(cnt):
    for i in range(5):
        card_five[cnt] = card_shake[cnt]
        cnt += 1
    print('뽑은 카드는 : ',card_five)
    print('남은 카드 수는 :',52 - cnt)
    return cnt

def card_print():
    print('뽑은 숫자는 : ',card_five)
    



card_shape = ['SPADE', 'DIAMOND', 'HEART', 'CLOVER']
card_num = [i for i in range(1,14)]
card_num[0] = 'A'
card_num[10] = 'J'
card_num[11] = 'Q'
card_num[12] = 'K'

card_shake = [[0]*2 for i in range(52)]  
card_five = [0 for i in range(5)]
cnt = 0


while True:
    print('[ 카드 프로그램 ]')
    print('1. 카드생성')
    print('2. 카드섞기')
    print('3. 카드5장 나눠주기')
    print('4. 카드5장 확인하기')
    print('-'*50)
    choice = int(input('원하는 번호를 입력하세요.>> '))

    if choice == 1:
        card_creat()
        
    elif choice == 2:
        card_shuffle()
        
    elif choice == 3:
        card_share(cnt)
        
    elif choice == 4:
        card_print()

    else:
        print('프로그램을 종료합니다.')
        break
