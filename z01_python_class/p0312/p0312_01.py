# 두 수를 입력받아, 두 수 사이의 합계를 구하시오.

# 1. 두 수 입력
# 2. 함수호출
# 3. 1, 10  > 1+2+3+4+5+6+7+8+9+10   합계를 리턴받아서 합계 : 55가 나오도록 출력


# def summery(s_list):

#     for i in range(s_list[0],s_list[1]+1):
#         pass
#         s_list[2] += i
#     # return ss
    
# ss = 0
# num1 = int(input('첫째 숫자를 입력하세요 >> '))
# num2 = int(input('둘째 숫자를 입력하세요 >> '))
# s_list = [num1,num2,ss]
# sum = summery(s_list)
# print(s_list[2])

# 1,10 >> 1~10까지의 더하기, 빼기, 곱하기의 결과값을 출력하시오.

def cal(num1,num2):
    if num1 > num2:
        num1,num2 = num2,num1
        
    for i in range(num1+1,num2+1):
        s_list[2] += i
        
    for i in range(num1+1,num2+1):
        s_list[3] -= i
        
    for i in range(num1+1,num2+1):
        s_list[4] *= i
        
num1 = int(input('첫째 숫자를 입력하세요 >> '))
num2 = int(input('둘째 숫자를 입력하세요 >> '))
sum = num1
min = num1
x = num1
s_list = [num1,num2,sum,min,x]

cal(num1,num2)

print('더하기 결과값 :', s_list[2])
print('빼기 결과값 :', s_list[3])
print('곱하기 결과값 :', s_list[4])














