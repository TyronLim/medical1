# 산술 연산자
# + - * /   
a = 4
b = 3
# result = a + b
# result = a - b
# result = a * b
# result = a / b

# result = 4 // 2   >> 몫 (2)
# result = 5%2      >> 나머지(1)
# print(result)
# result = a**b     >> 제곱
# print(result)

# 산술연산자 우선순위
# 곱셈, 나눗셈 먼저 이후 덧셈 뺄셈
# 괄호가 없을 경우 왼쪽에서 오른쪽 방향으로 계산
# r1 = 2 + 2 - 2 * 2 / 2 * 2      >>> 곱나눗부터 . 그러나 헷갈려서 괄호사용을 추천
# r2 = 2 - (2/2)  # 괄호 사용

# 다른 자료형으로 연산
# str1 = "문자열"
# n1 = 10
# print(str*n1)
# print(str1+n1)  >> 에러 (문자에 숫자를 더할 수 없기 떄문

# 문자열이 정수나 실수일 경우 int(),float()를 사용해서 변환
# s1 = "100"
# s2 = "10.123"
# print(int(s1)+1)
# print(float(s2)+1)

# n = int("안녕하세요")  >>>  숫자가 아닌 것을 변환 할 수 없다

# 숫자를 문자로 바꾸고 싶으면 str() 사용 
# n1 = 100
# n2 = 10.123
# print(str(n1)+'1')
# print(str(n2)+'1')
# # 핸드폰 같은 경우 처음 0이 들어가므로 사용
# p=12341234
# print("010"+str(p))

#나누기 값, 몫, 나머지 값 구하기
# 출력 >> 나누기 값 : (2.0), 몫 : (2), 나머지 : (0)

# a=10
# b=5
# print("나누기 값 :", a/b,"\t", "몫 :", a//b,"\t", "나머지 값 :", a%b)


# c= int(input('첫째 숫자 : '))
# d= int(input('둘째 숫자 : '))
# print('나누기 값 : {:.3f} \n 몫 값 : {} \n 나머지 값 : {}'.\
#     format(c/d,c//d,c%d))


# e = 33
# f = 11
# print ("제가 가능한 숫자는 %d이고 싫어하는 숫자는 %d입니다"%(e,f))
# print("둘을 더한 숫자는 {}이고, 둘을 뺀 숫자는 {}이다".format(e+f,e-f))

