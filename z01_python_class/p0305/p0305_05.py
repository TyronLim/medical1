# 1-25까지 숫자를 랜덤으로 섞은 다음, 2차원 리스트에 넣어보세요.
import random

num = random.randint(1,100)
print(num)

# 숫자맞추기 프로그램을 구현
# 1-10까지의 숫자 랜덤으로 생성, 숫자를 맞추는 프로그램입니다.
count = []
cnt = 0
while True:
    in_num = int(input('1-100까지의 숫자를 입력하세요. >> '))
    cnt += 1
    count.append(in_num)
    if num>in_num :
        print('입력한 숫자보다 더 큽니다. 더 큰 수를 입력하세요.')
        
    elif num<in_num :
        print('입력한 숫자보다 더 작습니다. 더 작은 수를 입력하세요.')
        
    else :
        print('정답!')
        print('{}번만에 맞추셨네요!'.format(cnt))
        break
print(count)