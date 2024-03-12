#해보세요 1
#나이가 10살 이상이고, 150 이상만 탑승가능
#나이, 키를 입력받아 [탑승가능] [탑승불가능]을 출력해보세요.

#해보세요 2
#숫자가 3개(정수)를 입력받고, 연산1개를 입력받아
#+++ --- *** /// (나누기값은 둘째자리까지 표현)
# a + b + c = d의 형태로 출력하시오

age = int(input('나이를 입력하세요 >'))
hight = int(input('키를 입력하세요  >'))

if age >= 10:
    pass
    if hight >=150:
        print('[탑승가능]')
    else:
        print('[탑승불가능]')    
else : 
    print('[탑승불가능]')


a = int(input('숫자1을 입력하세요 >>'))
b = int(input('숫자2를 입력하세요 >>'))
c = int(input('숫자3을 입력하세요 >>'))
y = input('연산기호를 입력하세요 >>')


if y == '+':
    print('{}+{}+{}={}'.format(a,b,c,a+b+c))
elif y == '-':
    print('{}-{}-{}={}'.format(a,b,c,a-b-c))
elif y == '*':
    print('{}*{}*{}={}'.format(a,b,c,a*b*c))
elif y == '/':
    print('{}/{}/{}={:.2f}'.format(a,b,c,a/b/c))

print()
