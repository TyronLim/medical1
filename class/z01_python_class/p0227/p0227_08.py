# 반복문
'''
for 변수 in range(시작값, 끝값+1, 증가값):
'''
# for i in range(3):      # i = 0, 1, 2
#     print('안녕')
#     # i = 0 일때
#     # i = 1 일때
#     # i = 2 일때
    
# for i in range(3):      # i = 0, 1, 2
#     print(i)
    
# i = 0,1,2,3 ...
# i = 1,2,3,4 ... 
for i in range(100):
    print(i+1)

sum1 = 0
for i in range(1,6,1):
    sum1 = sum1 + i

# 숫자 한개를 입력받아서 1부터 입력한 수 까지의 합을 구하세요.

n1 = int(input('숫자 하나를 입력하세요 >'))
num = 0
for i in range(1,n1+1):
    num += i
print(num)

# 짝수의 합만 구함 (2+4+6+8+...+100)
num2 = 0
for j in range(1,n1+1):
    if j%2 == 0:
        num2 += j
print(num2)

# 짝수의 합만 구하는 두 번째 방법 (2부터 시작해서 2씩 증가하는 변수 k)
num3 = 0
for k in range(2,n1+1,2):
    num3 += k
print(num3)

# 1-10 까지의 곱 구하기
num4 = 1
for n in range(1,11):
    num4 *= n     # 1*1 1*1*2 1*1*2*3 1*1*2*3*4 .... 1*1*2*3*4*5*6*7*8*9*10)
print(num4)