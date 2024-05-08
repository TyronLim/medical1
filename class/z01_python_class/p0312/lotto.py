import random



# -----------------------------------------------------------------------#
# 화면 출력 함수
def screen():
    print('[ 로또번호 맞추기 프로그램]')
    print('1. 번호생성')
    print('2. 번호섞기')
    print('3. 나의 번호 6개입력')
    print('4. 당첨번호 6개확인')
    print('-'*50)
    choice = int(input('원하는 번호를 입력하세요. >>'))
    
    return choice
#------------------------------------------------------------------------#
# 번호 생성 함수
def num_generate(lotto):
    
    print('번호생성')
    for i in range(45):
        lotto[i] = i+1
    # print(lotto)
    # a = [i for i in range(1,46)]
    # lotto.append(a)
#------------------------------------------------------------------------#
# 번호 섞기 함수
def num_shuffle(lotto):
    
    print('번호섞기')
    random.shuffle(lotto)
#------------------------------------------------------------------------#
# 나의 번호 6개 입력 함수
def num_input(myNum):
    for i in range(6):
        my = int(input(f'{i+1}번째 숫자를 입력하세요'))
        myNum[i] = my
#------------------------------------------------------------------------#
# 당첨번호 6개 확인 함수
def num_check(lotto,lotto2,myNum):
    # win_list = []   주소값을 다시 세팅
    print('당첨번호 6개 확인')    
    for i in range(6):
        lotto2 [i] = lotto[i]
    print('번호 확인')
#------------------------------------------------------------------------#
# 몇개 맞췄는지 확인 함수
def num_count(cnt,win_list):    
    cnt = 0
    for i in lotto2:
        for j in myNum:
            if j == i:
                win_list.append(j)
                cnt += 1
    print(f'맞춘 개수는 {cnt}개 입니다.')
    print(f'맞춘 숫자는 {win_list}입니다.')
    print(f'당첨 금액은 {win_amount[len(win_list)]}입니다.')
        
    # 당첨금액 출력
    # if cnt == 0:
    #     print(f'당첨금액은 {win_amount[0]}원 입니다.')
    # elif cnt == 1:
    #     print(f'당첨금액은 {win_amount[1]}원 입니다.')
    # elif cnt == 2:
    #     print(f'당첨금액은 {win_amount[2]}원 입니다.')
    # elif cnt == 3:
    #     print(f'당첨금액은 {win_amount[3]}원 입니다.')
    # elif cnt == 4:
    #     print(f'당첨금액은 {win_amount[4]}원 입니다.')
    # elif cnt == 5:
    #     print(f'당첨금액은 {win_amount[5]}원 입니다.')
    # elif cnt == 6:
    #     print(f'축하드립니다! 당첨금액은 {win_amount[6]}원 입니다.')
    
    return cnt,win_amount




lotto = [0]*45   # 1~ 45까지 랜덤하게 돌린 숫자
lotto2=[0]*6    #[0,0,0,0,0,0]  # 당첨번호 6개 숫자
myNum = [0]*6   # 내가 입력한 6개 숫자
win_list = []
win_amount = [0,0,1000,10000,1000000,100000000,10000000000]
cnt = 0