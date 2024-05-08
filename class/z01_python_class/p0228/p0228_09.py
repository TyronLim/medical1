# for문을 사용해서 2단을 출력
# 입력받은 숫자의 단을 출력하세요 

# for i in range(1,10):
#     print('2*{}={}'.format(i,2*i))

# n = int(input('숫자를 입력하세요 >> '))
# for i in range(1,10):
#     print('{}*{}={}'.format(n,i,n*i))
    
# 중첩 for
# for 안에 for

# for i in range(2,10):
#     for j in range(1,10):
#         print('{}*{}={}'.format(i,j,i*j))

#출력 형해 1 2 3 4 5
# for j in range(1,6):
#     print(j,'번째 출력')
#     for i in range(1,6):
#         print(i, end = ' ')
#     print()

# for i in range(2,10):
#     print('[{} 단]'.format(i))
#     for j in range(1,10):
#         print('{}*{}={}'.format(i,j,i*j),end = '  ')
#     print()

# # 짝수단만 출력해주세요
for i in range (2,10):
    if i%2 == 0 :
        print('[{} 단]'.format(i))
        for j in range (1,10):
            print('{} * {} = {}'.format(i,j,i*j),end = '    ')            
    print()

# (*1,*3,*5,*7,*9) 하는 것들만 출력
for i in range(2,10):
    print('[{} 단]'.format(i))
    for j in range (1,10):
        if j%2 != 0:
            print('{} * {} = {}'.format(i,j,i*j),end = '    ')
    print()

# 