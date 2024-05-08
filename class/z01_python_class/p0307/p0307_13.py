list = [
    [],[],[]
]
# 2차원 list. 크기가 지정이 안 됨.
# append로 리스트를 만드는 방법
a_list = []
a_list.append(0)    # 리스트에 append로 추가하면 속도가 느림
a_list.append(1)
a_list.append(2)
a_list[0] = 3       # 리스트에 값을 넣는 것이 속도면으로는 빠름
print(a_list)

# 공간을 만들어놓고 for문 사용
list2 = [0]*10
for i in range(10):
    list2[i] = i+1
print(list2)

# 컴프리헨션을 사용하는 방법
list1 = [n+1 for n in range(10)]