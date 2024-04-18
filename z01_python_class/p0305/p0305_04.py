a= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# print(a)

# for i in range(5):  # 0,1,2,3,4
#     for j in range(5):  # 0,1,2,3,4
#         a[i][j] = (5*i)+j+1    
# print(a)

# 2차원 리스트 입력
value = 1
for i in range(5):  # 0,1,2,3,4
    for j in range(5):  # 0,1,2,3,4
        a[i][j] = value
        value +=1
print(a)

# 좌표를 입력하면 0으로 변경하는 프로그램을 구현
while True:
    # 2차원 리스트 보기 좋게 출력
    print(0,'|',0,1,2,3,4,sep = '\t')
    print('-'*50)
    for i in range(0,5):
        print(i,'\t','|',end ='\t')
        # print(i,'\t','|',end='\t')
        for j in range(0,5):
            print(a[i][j],end ='\t')
        print()
    
    x = int(input('x 좌표를 입력하세요 >> '))
    y = int(input('y 좌표를 입력하세요 >> '))
    if 0 <= x <= 4: 
        if 0 <= y <= 4:
            a[x][y] = 'X'
            print('-'*35)
        
    else :
        print('올바른 숫자를 입력하세요.')