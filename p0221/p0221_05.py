# 변수
# int형
# 10진법 정수

var1 = 100
print(var1)
num1 = -100
print(var1-num1)

# 2진법 : 0b로 시작
num3 = 0b101010
# 2진법 규칙 = 1*2^5 + 0*2^4 + 1*2^3 + 0*2^2 + 1*2^1
print(num3)

# 8진법 : 0o로 시작
num4 = 0o52
print(num4)
# 8진법 규칙 = 5*8^1 + 2*8^0 = 40 + 2 = 42

#16진법 : 0x로 시작
# 1,2,3,4,5,6,7,8,9,a,b,c,d,e,f 의 수로 표현
num5 = 0x2a
print(num5)
# 16진법 규칙 = 2*16+10 = 32+10 = 42

#float 형 : 실수 즉 소숫점을 포함하고 있는 수
num6=3.14
print(num6)
print("%f"%num6)
num7 = 2 * 3.14 * 5
print(num7)

# complex 형 : 실수 + 허수
# 3+2i > 파이썬에서는 i 대신 j를 사용
comp1 = 3+4j
print(comp1)
print(comp1.real)
print(comp1.imag)

# boolean 형 : True, False
bool1 = True
bool2 = False
print("bool1 =",bool1)
print("bool2 =",bool2)
bool3 = (1==2)
print("bool3 =",bool3)

bool4 = (0x2a ==42)
print = ("bool4 =", bool4)

# String 형
str1 = "안녕하세요"
str2 = "Hello"
print(str1)
print(str2)

# list, tuple, dict, set 등이 있음