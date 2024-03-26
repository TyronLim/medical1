# a= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# a = [[0]*5]*5   # 얕은 복사
a = [[0]*5 for i in range(5)]  ## 컴프리헨션 복사
print(a)

# for i in range(5):  # 0,1,2,3,4
#     for j in range(5):  # 0,1,2,3,4
#         a[i][j] = (5*i)+j+1    
# print(a)

value = 1
for i in range(5):  # 0,1,2,3,4
    for j in range(5):  # 0,1,2,3,4
        a[i][j] = value
        value +=1
    
# print(a)
