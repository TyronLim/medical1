# 대입 연산자 =
a = 3
a = a+1
a += 1
# a+=1  >> a = a+1
# 그 밖에도 +=, -=, *=, /=, //=, %=, **=  가능. 좌변 우변이 동인한 변수명(a)일 경우 생략, 축약하는 방법이다.

a=3
b=2
a *= 2+b
# [a *= 2+b]  >> a = a*(2+b)   **헷갈리지 않도록 주의

# 20에서 시작해서 값 누적되어서 출력됨 (print 기준 마지막 값으로)
num = 20
num += 2
print(num)
num -= 2
print(num)
num *= 2
print(num)
num /= 2
print(num)