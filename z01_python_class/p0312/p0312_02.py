# 1. 번호생성
# 2. 번호섞기
# 3. 번호뽑기
# 4. 번호확인

import lotto

    





lotto = [0]*45   # 1~ 45까지 랜덤하게 돌린 숫자
lotto2=[0]*6    #[0,0,0,0,0,0]  # 당첨번호 6개 숫자
myNum = [0]*6   # 내가 입력한 6개 숫자
win_list = []
win_amount = [0,0,1000,10000,1000000,100000000,10000000000]
cnt = 0

while True:
    choice = lotto.screen()                   # 화면출력함수 호출
    
    if choice == 1:
        lotto.num_generate(lotto)             # 번호생성함수 호출
        print(lotto)
            
    elif choice == 2:
        lotto.num_shuffle(lotto)              # 번호섞기함수 호출
        print(lotto)
        
    elif choice == 3:
        lotto.num_input(myNum)
        print('내가 선택한 숫자 :',myNum)
        
    elif choice == 4:
        lotto.num_check(lotto,lotto2,myNum)
        print('당첨 번호 :', lotto2)
        print('선택 숫자 :', myNum)

        lotto.num_count(cnt,win_list)
        win_list = []
        
    