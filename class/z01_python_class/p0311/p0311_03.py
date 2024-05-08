# 구구단 - 이중 for 문을 사용하고 있음.
cnt = 0

for i in range(1,10):
    
    for j in range(1,10):
        if j == 5:
            cnt = 1
            break
            
        print(f'{i}*{j}={i*j}')
    
    if cnt == 1:
        break