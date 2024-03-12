# 반복문
# print('안녕하세요')
# print('안녕하세요')
# print('안녕하세요')
# print('안녕하세요')
# print('안녕하세요')

# '''
# for 변수 in 반복가능한 데이터:
#     수행할 문장
# '''

# # 순차적으로 커질 때 range를 사용한다.
# for i in range(0,5,1):  # range(시작값,끝값+1,증가값)
#     print('안녕')       # i 가 0,1,2,3,4
# for i in range(0,5,1):  # range(시작값,끝값+1,증가값)
#     print(i,'안녕')       
    
# for i in range(0,3) :  # 증가값이 1일 경우 생략 가능
#     print(i,"Hi")

# for i in range(4):      #n번 반복할 경우 range(n)을 사용할 수 있다.
#     print('hello')
# for _ in range(2):        # i를 사용하지 않을 경우 _ 사용할 수 있다.
#     print('반갑습니다.')
    
# for i in range(5):
#     num = int(input('숫자를 입력하세요>>'))
#     print('입력하신 숫자는 : {}'.format(num))
    
# i,j 카운터 변수 (k, l ...)   > i,j 를 자주 사용
# 카운터 변수는 반복 실행 될 때마다 현재 실행 횟수에 해당하는 숫자가 들어감.
# 가장 처음은 실행한 적이 없으므로 0이 된다.

# for i in range(3):
#     print(i)

# str1 = '안녕하세요'
# for i in str1:
#     print(i)

# 1에서부터 15까지 출력해보세요
for i in range(1,16,1):
    print(i)
    
#10을 4번 반복해서 출력해보세요
for i in range(4):
    print(10)

#helloworld를 6번 반복해서 출력해보세요
for i in range(6):
    print('helloworld')
    
#1-100 사이 2의 배수를 출력해보세요.
for i in range(2,101,2):
    print(i)
    #print(i, end=' ')   1줄로
    
#print()   >  줄바꿈

#1-100 사이 5의 배수를 출력해보세요.
for i in range(5,101,5):
    print(i)



