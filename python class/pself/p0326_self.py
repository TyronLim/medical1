import random
lotto = [i+1 for i in range(45)]
random.shuffle(lotto)
print(lotto)

lotto_num = []
for i in range(6):
    lotto_num.append(lotto[i])

print(lotto_num)

my_num=[]
for i in range(6): 
    a = int(input(f'{i}번째 숫자를 입력하세요 >> '))
    my_num.append(a)

print(my_num)

correct=[]
for i in lotto_num:
    for j in my_num:
        if i == j:
            correct.append(i)

print('맞힌 숫자는 {}입니다.'.format(correct))
print('총 {}개 맞혔습니다.'.format(len(correct)))
