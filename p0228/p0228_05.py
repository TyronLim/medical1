n1 = int(input('첫번째숫자 >> '))
n2 = int(input('두번째숫자 >> '))
sum = 0
# n1 부터 n2 까지 합을 구해보세요

for i in range (n1,n2+1):
    sum += i
print(sum)

# n1, n2 비교해서 작은 수를 n1에 넣기
sum2 = 0
if n1 < n2:
    for j in range (n1, n2+1):
        sum2 += j
elif n1 > n2:
    for j in range (n2, n1+1):
        sum2 += j
else :
    sum2 = n1
print(sum2)

# n1, n2 비교해서 작은 수를 n1에 넣기 두번째 방법
sum4 = 0
if n1 > n2:
    n1, n2 = n2, n1
    for _ in range(n1, n2+1):
        sum4 += _
else :
    for _ in range(n1, n2+1):
        sum4 += _
print(sum4)


# n1-n2까지의 홀수 값을 저장
odd_list = []
sum3 = 0
for k in range (n1,n2+1):
    if k%2 != 0:
        odd_list.append(k)
print(odd_list)
