import random

card_num = [i for i in range(1,14)]

# 랜덤으로 2개의 숫자를 뽑아서 출력하시오.
a = random.sample(card_num,2)
print(a)

for i,k in enumerate(card_num):    
    if a[0] < a[1]:
        for j in a:
            if j == k:
                print(f'{j}는 {i}번 방에 있습니다.')
    else:
        for j in range(len(a)-1,-1,-1):
            if a[j]==k:
                print(f'{a[j]}는 {i}번 방에 있습니다.')   



# if a[0] > a[1]:
#     print(f"큰수={a[0]}, 작은수={a[1]}")

# else:
#     print(f"큰수={a[1]}, 작은수={a[0]}")


# for j in range(len(a)-1,-1,-1):
#     print(j)
#     if a[j]==card_num:
#         print(f'{a[j]}는 {0}번 방에 있습니다.')   