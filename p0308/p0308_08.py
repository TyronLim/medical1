import random

f_num = random.randint(1,9)
l_num = random.randint(0,999999)


lotto = str(f_num)+'조'+ str('{:06d}'.format(l_num))      # 자리수 맞춰서 넣기

l_input = input('복권을 입력하세요.(예 :1조111111)')

motto = '{}조{}{}{}{}{}{}'.format(l_input[0],l_input[1],l_input[2],l_input[3],l_input[4],l_input[5],l_input[6])

cnt = 0
print(lotto)
for i in range(len(lotto),0,-1):
    if lotto[i-1] == motto[i-1]:
        cnt += 1
     
if cnt == 0:
    print('완전 꽝입니다.')
