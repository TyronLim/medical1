
n = int(input('숫자를 입력해주세요 : '))
if n > 100: 
    print('100보다 큽니다.')
elif n == 100:
    print('100입니다.')
else: 
    print('100보다 작습니다.')


if n%2==0 : 
    print('짝수입니다.')
else : 
    print('홀수입니다.')
    
if n >= 7:
    print('합격')
else :
    print('불합격')
    
if n < 10 and n > 5 :  # 5 < n < 10
    print('5보다 크고 10보다 작은 수입니다.')
else :
    print('5보다 작거나 10보다 큰 수입니다.')
    
if n%3 ==0 : 
    print('3의 배수입니다.')
    
else : 
    print('3의 배수가 아닙니다.')
    
if n%2==0 and n%3==0 :
    print('2의 배수이며 동시에 3의 배수입니다.')
else :
    print('2의 배수임과 동시에 3의 배수가 아닙니다.')
    
if n%2==0:
    print('2d의 배수입니다.')
elif n%3==0 :
    print('3의 배수입니다.')
else :n%2!=0 and n%3!=0 
print('2의 배수도, 3의 배수도 아닙니다.')