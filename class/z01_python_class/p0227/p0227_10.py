num=[] 
# for 문을 사용해서 1-10 까지 숫자를 num에 채우세요
for i in range(1,11):
    num.append(i)


num2=[]
#1-10까지의 짝수를 num2리스트에 넣으세요
for i in range(1,11):
    if i%2 == 0 :
        num2.append(i)

# num1 = [i for i in range(1,11)]      # 1~10 까지 리스트에 넣는 방법2

# 1~10 까지의 합 for 문을 사용해서 구한 다음

# num리스트를 사용해서 1-10까지의 합을 구해보세요.
n = 0
for i in num:
    n += i
print(n)

m = 0
for i in range(len(num)):
    m += num[i]
print(m)

# num2리스트를 사용해서 1-10까지의 합을 구해보세요.
a = 0
for i in num2:
    a += i
print(a)

b = 0
for i in range(len(num2)+1):
    b += (i*2)
print(b)

c = 0
for i in range(len(num2)):
    c += num2[i]
print(c)

