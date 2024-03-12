# 리스트에 1, 25까지의 숫자를 입력하시오.

list = []
for i in range(25):
    list.append(i+1)
# print(list)

# 1부터 25까지 2차원 리스트 생성
# [[1,2,3,4,5],[6,7,8,9,10],...,[21,22,23,24,25]]

list2 = []
a = []
for i in range(1,26):
    if i%5 == 0:
        a.append(i)
        list2.append(a)
        a = []
    
    else:
        a.append(i)
print(list2)








