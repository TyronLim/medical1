num = [100,200,300,400]
# for 문을 사용해서 하나씩 출력
'''
for i in range(len(num)):
    print(num[i])

for i in num:
    print(i)
'''
'''
numlist = [[1,2],[3,4],[5,6]]
for i in numlist:
    for j in i:
        print(j)
        
for i in range(len(numlist)):
    for j in range(len(numlist[i])):
        print(numlist[i][j])

'''
f = [['딸기',100,1000],['수박',100,500],['사과',100,1200],['귤',100,300]]

for i in f:
    # print(i)
    for j in i:
        print(j)
        
for i in range(len(f)):
    for j in range(len(f[i])):
        print(f[i][j])

# score = [90,80,70,100,95,85,100]
# total = []
# # 점수의 총합을 구하세요
# a = 0
# for i in range(len(score)):
#    a = a + score[i]
# total.append(a)
# print(total)










