# 리스트
list = []

# 1- 10까지 숫자를 입력해보세요.
# 컴프리헨션
list = [i+1 for i in range(10)]
print(list)

# for문 append
# for i in range(10):
#     list.append(i+1)
# print(list)

list = [[]]*10
print(list)
for i in range(10):
    list[i] = i+1

print(list)




