# continue 예제
# 1 - 100 합계를 구하는데 3의 배수는 제외하고 더하기

i = 0
sum = 0
while i<100:
    i += 1
    if i%3==0:
        continue
    sum +=i
print(sum)

sum2 = 0
for i in range(1,101):
    if i % 3 == 0:
        continue
    sum2 += i
print(sum2)