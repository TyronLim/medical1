cal = input('수식을 입력하세요 (+,-,*,/) >> ')
n1 = 24
n2 = 5

if cal == '+' or cal == '-' or cal == '*' or cal == '/' :  # 삭제 가능
    if cal == '+':
        print(n1 + n2)
    elif cal == '-':
        print(n1 - n2)
    elif cal == '*':
        print(n1 * n2)
    elif cal == '/':
        print(n1/n2)
else :
    print ('수식을 제대로 입력하세요')
    

