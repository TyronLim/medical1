import random
random_num = random.randint(10000,99999)

print('[랜덤숫자 맞추기]')
print('랜덤숫자 : ',random_num)
a_input = input('숫자 5자리를 입력하세요')

# 숫자 자리로 확인해서 맞춘 개수를 출력하시오.

random_num = str(random_num)



cnt = 0
for i in range(len(random_num),0,-1):
    if random_num[i-1] == a_input[i-1]:
        cnt += 1
    else :
        break

if cnt == 0:
    print('꽝')

elif cnt == 1:
    print('{}개'.format(cnt))
    
elif cnt == 2:
    print('{}개'.format(cnt))
    
elif cnt == 3:
    print('{}개'.format(cnt))
    
elif cnt == 4:
    print('{}개'.format(cnt))
    
elif cnt == 5:
    print('{}개'.format(cnt))

