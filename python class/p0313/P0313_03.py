import random
# 랜덤으로 숫자 1개를 생성
# 입력한 숫자보다 크면 작은 수를 입력하시오
# 입력한 숫자보다 작으면 큰 수를 입력하시오. 라고 멘트가 나오게 하기
# 정답을 맞추면 횟수, 숫자를 모두 출력하시오.
# 총 입력한 횟수 : 0회
# 현재까지 입력한 숫자 : 1,3,5,6,8,9,30
def rand(num_ran):
    while True:
        num_input = int(input('숫자를 입력하세요'))
        num_list.append(num_input)
        if num_ran > num_input:
            print('더 큰 수를 입력하세요.')
            
        elif num_ran < num_input:
            print('더 작은 수를 입력하세요.')

        elif num_ran == num_input:
            print('정답입니다.')
            break

num_list = []
num_ran = random.randint(1,100)
rand(num_ran)

print('총 입력한 횟수 :',len(num_list))
print('입력한 숫자 :',num_list)
