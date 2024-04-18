'''    
반복문 - for, while 
for 변수 in 반복가능한데이터:
    수행문    
for 카운터변수 in range(시작값, 끝값+1, 증감값):
    수행문
'''
for i in range(0,10,1): # 0,1,2,3,4,5,6,7,8,9  총 10번
    print('수행문입니다')

for i in range(0,10,2): # 0,2,4,6,8,(9)  총 5번
    print('증감2 : 수행문입니다.')
    
for i in range(0,3):  # 증감값이 1일때는 생략 가능
    print('두 번째 수행문입니다.')

for i in range(5):   # 0부터 시작 시 생략 가능
    print('세번째 수행문입니다.')
    
print('-'*35)
for i in range(3):
    print(i)
    
# 카운터변수 i를 사용하지 않을 때 _로 사용 가능
for _ in range(7):  # 안녕하세요 7번 반복
    print('안녕하세요')

for i in range(10,1,-2):  # 앞 숫자가 커야 함  초과
    print(i,'증감')

l1 = [100,200,300,400,500]
'''
for 변수 in 리스트명
    실행문

for 변수 in range(len(리스트명))
    실행문
    리스트명[변수]
'''
for n in l1:
    print(n)

for i in range(len(l1)):
    print(i)   # 0,1,2,3,4
    print(l1[i]) #l1[0], l1[1], l1[2] ....
    
# for문을 사용해서 1-100 사이의 홀수를 출력해보세요
# 1) if 사용하지 않음
for i in range(1,101,2):
    print(i)
    
# 2) if 사용
for j in range(1,100):
    if j%2==1:
        print(j)
        
# 50 - 1 사이의 6의 배수를 역순으로 출력해보세요
for _ in range(48,1,-6):
    print(_)
    
for k in range(50,1,-1):
    if k%6 == 0:
        print(k)

# # print('-'*40)
# for t in range(-5,5,1):
#     if t%2 == 1:
#         print(t)
    
#input() 사용
# 입력 : 두개의 숫자를 입력받음
# 출력 : 사칙연산 
'''
a + b = c
a - b = d
a * b = e
a / b = f
'''
# 계산을 10번 반복하는 코드를 만드세요.

#

for i in range(10):
    a = int(input('숫자1 >>'))
    b = int(input('숫자2 >>'))
    c = input('연산자 >>')
    if c == '+':
        print('{}{}{}={}'.format(a,c,b,a+b))
    elif c == '-':
        print('{}{}{}={}'.format(a,c,b,a-b))
    elif c == '*':
        print('{}{}{}={}'.format(a,c,b,a*b))
    elif c == '/':
        print('{}{}{}={:.2f}'.format(a,c,b,a/b))
    else :
        print('다시 입력하세요')