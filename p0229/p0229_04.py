# 숫자 두 개를 입력받고
# 연산자를 입력받아서 (+-*/)
# 무한히 계산하는 계산기를 만드는데
# 첫번째 숫자게 0을 입력하면 프로그램이 종료가 되는 코드를 만드세요.

while True:
    a = int(input('첫째 숫자를 입력하세요>> '))
    if a == 0:
        print('계산기가 종료되었습니다.')
        break
    c = input('연산자를 입력하세요')
    b = int(input('둘째 숫자를 입력하세요>> '))
    
    if c == '+':
        print('{}+{}={}'.format(a,b,a+b))
    elif c == '-':
        print('{}-{}={}'.format(a,b,a-b))
    elif c == '*':
        print('{}*{}={}'.format(a,b,a*b))
    elif c == '/':
        print('{}/{}={:.3f}'.format(a,b,a/b))
