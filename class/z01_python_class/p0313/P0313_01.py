# 함수선언 def 이름() 정의
# 함수값은 return
# 함수호출 이름()
# 매개변수 : 함수로 데이터 전달하는 변수. 매개변수 개수는 항상 같아야 한다.
# 가변매개변수선언 #values, 가변매개변수 개수는 일치하지 않아도 된다.
# 리스트, 딕셔너리는 주소값이 전달이 된다.

# 퀴즈1
# 함수를 사용하여 두수를 입력받아 더하기, 빼기, 곱하기, 나누기 결과값을 출력하시오.
# 두수입력을 받아 값을 리턴 받은 다음, 출력하시오.

def cal(num1,num2):
    sum = num1 + num2
    min = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    
    result = sum,min,mul,div
    return result


num1 = int(input('첫째 숫자를 입력하세요 >> '))
num2 = int(input('둘째 숫자를 입력하세요 >> '))
result = cal(num1,num2)

print(result)

#-----------------------------------------------------------------------------------#

# def cal2(num1,num2,c):
#     if c == '1':
#         result = num1+num2
    
#     elif c == '2':
#         result = num1-num2

#     elif c == '3':
#         result = num1*num2

#     elif c == '4':
#         result = num1/num2

#     return result

# num1 = int(input('첫째 숫자를 입력하세요 >> '))
# num2 = int(input('둘째 숫자를 입력하세요 >> '))
# c = input('1.더하기 2.빼기 3.곱하기 4.나누기')

# result = cal2(num1,num2,c)
# print(result)

