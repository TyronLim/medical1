import random
# 주택복권
# 4조740

# lotto = '1조740'
# # 예: 2조711 >> 1개번호가 맞았습니다.
# # 비교하는 프로그램을 구형하시오.
# l_input = input('복권을 입력하세요.(예 :1조111)')

# # for i in range(lotto):
# #     print(i)
        
# cnt = 0
# for i in range(len(l_input)):
#     if l_input[i] == lotto[i]:
#        cnt += 1 
   
# print(lotto)
# print(l_input)
# print('{}개를 맞혔습니다.'.format(i))

# 1조000000 ~ 9조999999

f_num = random.randint(1,9)
l_num = random.randint(0,999999)
lotto = str(f_num)+'조'+ str('{:06d}'.format(l_num))      # 자리수 맞춰서 넣기

l_input = input('복권을 입력하세요.(예 :1조111111)')

print(l_input)

import random

a='1조123456'
b='9조123456'
cnt = 0
for i in range(len(a),0,-1):
    if i == 2: continue   # 조는 건너뛰기
    if a[i-1] != b[i-1]:
        break
    else:
        cnt+=1

if cnt == 0:
    print('완전 꽝입니다.')





