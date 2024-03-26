# 인덱싱[0], 슬라이싱[0:4][:3][2:], len, upper, lower, swapcase, title


# a = input('문자를 입력하세요.')
# print('현재 입력한 문자 길이 : ',len(a))

# a = [1234,11111,1,145,20,1323456547]
# # 리스트의 각 숫자의 길이를 출력하세요
# for i in a:
#     i = str(i)
#     print(len(i))

# #짝수만 문자길이를 출력하세요
# for i in a:
#     if i%2 == 0:
#         i = str(i)
#         print('짝수는 {}이고, 길이는 {}입니다.'.format(i,len(i)))

# a = 1000000
# b = '안녕하세요.반갑습니다.저는 홍길동입니다.'
# print(len(b))

# print(len(str(a)))
# print(b[5])
# print(b[2:5])

# 한글자씩 출력을 해보세요
# title = '혼자공부하는파이썬수업'
# for i,j in enumerate(title):
#     print('{}번째는 {}'.format(i,j))

# title = input('문자를 입력하세요')
# for i in range(len(title)): #5
#     print(title[(len(title)-1)-i],end ='')
    
# 문자.upper()
# 문자.lower()
# 문자.swapcase()
# 문자.title()

shape_list = ['spadE','diamonD','heart','clover']
for i in shape_list:
    print(i.swapcase())





