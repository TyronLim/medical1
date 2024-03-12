# 1-100까지 더하는데,
# 총 합이 100이 넘었을 때 수를 출력하세요.

sum = 0
i = 1
while i < 101:
    sum = sum+i
    if sum > 100:
        break
    i = i+1
print(sum)
print(i)


sum2 = 0 
for i in range(100):
    sum2 += i
    if sum2 > 100:
        break
print(sum2)
print(i)



# sum = 0
# i = 1
# while i <= 100:
#     sum = sum+i
#     if sum > 100:
#         break
#     i = i+1
#     # print(sum)
#     print(i)


