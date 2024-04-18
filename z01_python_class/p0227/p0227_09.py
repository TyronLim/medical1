# print('2단 출력')
# for i in range(1,10):
#     print(' 2 * {} = {} '.format(i,2*i))
    
# 원하는 단을 입력받아서 (3 > 3단 출력)

n = int(input('구구단 몇 단 >'))
print('구구단 {}단 시작~!'.format(n))
for i in range(1,10):
    print('{} * {} = {}'.format(n,i,n*i))

# # 10번 반복

for i in range(5):
    n2=int(input('구구단 몇 단 >'))
    for j in range(1,10):
        print('{} * {} = {}'.format(n2,j,n2*j))

