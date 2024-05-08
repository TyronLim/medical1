#변수
a = False
b = 123
c = 1.3456
d = '문자'
e = [1,2,3,'문자']  # 리스트

# 출력
# print('안녕하세요')
# print(123*456)
# str1 = '반갑습니다'
# print(str1)  # 변수 사용
# print('{0:s} : {1:d} / {2:d} = {3:f}'.format(
#     '수식',7,3,7/3))
# print('{} : {} / {} = {}',format('수식',7,3,7/3))

# 관계연산자
# > : 크다, >= : 크거나 같다, < : 작다, <= : 작거나 같다
# == : 같다, != : 같지 않다

print(3>5)  # False
n1 = 10
n2 = 8
print(n1 != n2) # True
print(3 < n1 < 100) # True

#if n1 < 10

# 논리연산자 : and or not
a , b = 10, 9
print('and연산자')

if a == 10 and b == 9 :
    print('참 and 참 = 참')
else : 
    print('참 and 참 = 거짓')

if a == 10 and b != 9 :
    print('참 and 거짓 = 참')
else:
    print('참 and 거짓 = 거짓')
    
if a != 10 and b == 9 :
    print('거짓 and 참 = 참')
else : 
    print('거짓 and 참 = 참')
    
if a!= 10 and b!= 0:
    print('거짓 and 거짓 = 거짓')
else:
    print('거짓 and 거짓 = 거짓')


print('or연산자')

if a == 10 or b == 9 :
    print('참 and 참 = 참')
else : 
    print('참 and 참 = 거짓')

if a == 10 or b != 9 :
    print('참 and 거짓 = 참')
else:
    print('참 and 거짓 = 거짓')
    
if a != 10 or b == 9 :
    print('거짓 and 참 = 참')
else : 
    print('거짓 and 참 = 참')
    
if a!= 10 or b!= 0:
    print('거짓 and 거짓 = 거짓')
else:
    print('거짓 and 거짓 = 거짓')
    
print('not 연산자')
if not a == 10:
    print('not 참 = 참')
else :
    print('not 참 = 거짓')

if not a != 10 : 
    print('not 거짓 = 참')
else :
    print('not 거짓 = 거짓')
    
# 조건문 if
# if 조건문1:
#    실행문1
# elif 조건문2:
#       실행문2
# else :
#       실행문3
# 조건문1이 참이면 실행문1을 실행 후 종료
# elif가 있으면 (조건문1이 거짓이고 조건문 2가 참이면) 실행문2 실행 후 종료
# 조건문1, 2 가 거짓이면 실행문3 실행 후 종료

num = 5
if num > 0:   # 숫자가 0 이상이면 양수를 출력하시오.
    print('양수입니다.')
else :
    print('음수입니다')  # 그 외는 음수이므로 음수를 출력하시오.

#0,양수,음수 출력 하고플떄
if num > 0:
    print('양수입니다.')
elif num < 0:
    print('음수입니다.')
else :
    print('0입니다.')

# 실행문을 비우고 싶을 때: pass
if 1==1 :
    pass
else:
    print('else문 실행') # 참이므로 아무것도 출력 안 됨
    
# 중첩 if문(if문 안에 if문 사용)
if num >=0 : 
    if num == 0:
        print('0입니다')
    else :
        print('양수입니다')
else:
    print('음수입니다')




