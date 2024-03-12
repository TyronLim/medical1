# [[0],[0],[0],[0].....] 52개 만들기

# 1차원 리스트 생성방법
# a = [0 for i in range(52)]
# b = []
# for i in range(52):
#     b.append(0) 
# c = [0]*52
# print(a)
# print(b)
# print(c)

# 2차원 리스트 생성방법
# aa = [[0]*2]*52      # 얕은 복사
# aa[0][1] = 1
# print(aa)

# bb = [[0]*2 for i in range(52)]
# bb[51][0] = 1
# print(bb)

# cc = []
# for i in range(52):
#     dd = []
#     for j in range(2):
#         dd.append(0)
#     cc.append(dd)

# print(dd)
# print(cc)