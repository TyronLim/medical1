# 1~5까지의 합계를 구하세요

# sum = 1+2+3+4+5
# print(sum)

# total = 0
# total = total + 1   # 0+1
# total = total + 2   # 0+1+2
# total = total + 3   # 0+1+2+3
# total = total + 4   # 0+1+2+3+4
# total = total + 5   # 0+1+2+3+4+5
# print(total)

# t = 0
# for i in range(1,6,1):
#     t= t+i
#     print(t)
# print(t)            # 0+1 0+1+2 0+1+2+3 0+1+2+3+4 0+1+2+3+4+5

# # 1에서 10 까지의 합을 구해보세요 for
# a=0
# for i in range(1,11):
#     a+=i
# print(a)

# # 1에서 100까지 합을 구해보세요
# b=0
# for i in range(1,101):
#     b+=i
# print(b)

# 입력한 수부터 입력한 수까지의 합을 구해보세요

# n1 = int(input('첫째 숫자를 입력하세요 >'))
# n2 = int(input('둘째 숫자를 입력하세요 >'))
# num = 0
# for i in range(n1,n2+1,1):
#     num += i
# print(num)


q = 0
for i in range(3,6,1):   # i = 3,4,5
    q += i               # 0+3 0+3+4 0+3+4+5
    print(q)