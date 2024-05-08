# #1. 변수선언
score = [[80,90,85],[70,80,90],[84,92,80],[72,81,76]]
name = ['홍길동','유관순','이순신','김구']
total = []
# # 2. 코딩
# # 2-1) 요소 하나하나 출력해보세요 80 90 85 70 80 90 ...
# for i in score:
#     for j in i:
#         print(j,end = ' ')
# print()

# for i in range(len(score)):
#     for j in range(len(score[i])):
#         print(score[i][j], end = ' ')
# print()

# score = [[80,90,85],[70,80,90],[84,92,80],[72,81,76]]
# # 2-2) 작은 요소의 합을 구해서 total에 넣어주세요 
# # for i in range(len(score)):
# #     a = 0
# #     for j in range(len(score[i])):
# #         a = a + score[i][j]
# #     # print(a)
# #     total.append(a)

# for i in score:
#     a = 0
#     for j in i:
#         a = a + j
#     print(a)
#     total.append(a)

# # 3. 출력
# # 3-1) total = [255,240,256,229]
# print(total)

# # 3-2) 250 미만 불합격, 250이상 합격 (홍길동님 합격입니다) 출력
# for i in range(len(total)):
#     if total[i] >= 250 :
#         print('{}님 합격입니다.'.format(name[i]))
#     else :
#         print('{}님 불합격입니다.'.format(name[i]))
        
        
        
        

# 하나하나 출력
# for i in score:
#     for j in i:
#         print(j)                    >> 출력 
        
# for i in range(len(score)):
#     for j in range(len(score[i])):
#         print(score[i][j])          >> 출력

for i in range(len(score)):
    for j in score[i]:
        print(j)                    

score = [[80,90,85],[70,80,90],[84,92,80],[72,81,76]]
name = ['홍길동','유관순','이순신','김구']
total = []
# 2-2) 작은 요소의 합을 구해서 total에 넣기 
# for i in score:
#     a = 0
#     for j in i:
#         a = a + j
#     print(a)
#     total.append(a)
# print(total)                          >> 완료

# for i in range(len(score)):
#     a=0
#     for j in range(len(score[i])):
#         print(j)
#         a += score[i][j]
#     print(a)
#     total.append(a)
# print(total)                          >> 완료

# for i in range(len(score)):
#     a=0
#     for j in score[i]:
#         a+= j
#     print(a)
#     total.append(a)
# print(total)                          >> 완료