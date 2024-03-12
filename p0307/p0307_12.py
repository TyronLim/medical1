list = [
    [0,0,0],[0,0,0],[0,0,0]
]

# 1차원 리스트에 1-9까지의 숫자를 입력하시오.
list = []

for i in range(9):
    list.append(i+1)
print(list)    

list2 = [n+1 for n in range(9)]            ### 컴프리헨션
print(list2)

list3=[[0]*3 for n in range(3)]

print(list3)

numList = [num*num for num in range(1,6)]    # 제곱근 컴프
print(numList)

    
# 2차원 리스트에 1-9까지 숫자를 입력하시오.
# list2 = []
# for i in range(3):
#     list3 = []
#     for j in range(3):
#         list3.append((3*i)+j+1)
#     list2.append(list3)
    
# print(list2) 
    
    

    
    
    
    
    
# for i in list:
#     for f in i:
#         print(f, end= '\t')
#     print()