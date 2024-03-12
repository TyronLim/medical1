# 0 - 20 사이의 5의 배수로 이루어진 리스트를 만들어보세요
# [0,5,10,15,20]
# num = []

# for i in range(0,21):
#     if (i)%5 == 0:
#     #  print(i)
#         num.append(i)     
# print(num)

# for i in range(0,21,5):
#     num.append(i)
# print(num)

# lan = ['c','python','java','jquery','css']

# # 1. 하나하나 출력해보기
# for i in lan:
#     print(i)

# for i in range(len(lan)):
#     print(lan[i])


# # 2. 다음과 같이 출력해보기
# '''
# 1.c
# 2.python
# 3.java
# 4.jquery
# 5.css
# '''
# for i in range(len(lan)):    # = for i in range(5)
#     print('{}. {}'.format(i+1,lan[i]))

num = [1,-1,2,3,-4,5,6,-8,9,-10]
# 양수면 양수, 음수면 음수
# 1: 양수
# -1: 음수
# 2: 양수   ...

# for i in range(len(num)):
#     if num[i] > 0:
#         print('{}: 양수'.format(num[i]))
#     elif num[i] < 0:
#         print('{}: 음수'.format(num[i]))
#     else :
#         print('{}: 0'.format(num[i]))

# for i in range(10):
#     if num[i] > 0:
#         print('{}: 양수'.format(num[i]))
#     elif num[i] < 0:
#         print('{}: 음수'.format(num[i]))
#     else:
#         print('{}: 0'.format(num[i]))

for i in num:
    if i > 0:
        print('{}: 양수'.format(i))
    elif i < 0:
        print('{}: 음수'.format(i))
    else:
        print('{}: 0'.format(i))