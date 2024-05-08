# # 1-100까지의 합을 구하시오
# n = 0
# for i in range(1, 101):
#     n += i    
# print(n)

# # 1-100까지의 짝수의 합
# n2 = 0
# for i in range(1, 101):
#     if i%2 == 0:
#         n2 += i
# print(n2)

# # 1-100까지의 홀수의 합
# n3 = 0
# for i in range(1, 101):
#     if i%2 != 0:
#         n3 += i
# print(n3)

# 1-10 합
n4 = 0
for i in range(1,11):
    n4 += i
print(n4)

# 1-10을 리스트에 넣어서 그 안의 값 >> num = [1,2,3,4,5,6,7,8,9,10]
n5 = 0
num = []
for i in range(1,11):
    num.append(i)
    
for i in range(len(num)):
    n5 += num[i]
print(num)
