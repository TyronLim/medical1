# 변수 bool, int, float, string 타입
a = False #bool은 참 아님 거짓
b = 300 # int정수
c = 3.13 # float실수
d = '문자열' #string 문자열

# input() >> 콘솔창에서 입력을 받는다.
# e = input('입력하세요') # input 문자열로 입력을 받는다.
# print(e)

'''
if 조건문1:
    실행문1
elif 조건문2:
    실행문2
else :
    실행문3

>> elif, else는 생략이 가능
if를 건너뛰고 싶은 경우는 pass를 사용
ex) if 조건문:
        pass
'''
n= 10 #int(input('숫자를 입력해주세요 >>'))
if n >= 0 :
    print('양수')
    if n%2 == 0 :
        print('짝수')
    else :
        print('홀수')
else:
    print('음수')   
'''
반복문
for 변수 in 반복가능한 데이터:
    실행문
'''
# 순차적으로 커질 때는 range를 사용한다.
for i in range(0,3,1): # range(시작값, 끝값+1, 증감값)
    print('hi')        # i가     0      2+1      1
    # i = 0 일때, hi
    # i = 1 일때, hi
    # i = 2 일때, hi    총 3번 출력
    
for i in range(5): # i가 0부터 4까지 반복 = 5번 반복
    print(1)
    
for i in range(1,11):
    print(i)

print('-'*35)
a = 10
b = '안녕하세요'
#a, b 를 5번 반복해서 출력
for i in range(5): # i는 0-4
    print(i)
    a = a+1
    print(a)
    print(b)
# i = 0, i = 0, 10 + 1 > 11
# i = 0, i = 0, 11 + 1 > 12
# i = 0, i = 0, 12 + 1 > 13  ...

# 입력 : 이름, 점수 (5명의 이름과 점수를 입력받습니다.)
# 60점 이상이면 합격, 60점 미만이면 불합격을 출력하는데
# 출력의 형태는 [홍길동님 합격입니다][홍길동님 불합격입니다]



for i in range(5):
    name = input('이름을 입력하세요 >') 
    score = int(input('점수를 입력하세요 >'))    
    if score >= 60 :
        print('{}님 합격입니다.'.format(name))
    elif score < 60:
        print('{}님 불합격입니다.'.format(name))













