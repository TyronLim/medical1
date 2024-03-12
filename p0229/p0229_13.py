member = [[1,'홍길동'],[2,'유관순'],[3,'이순신']]

for i, j in enumerate(member):
    print(i)



# search2 = input('삭제할 학생의 이름을 입력해주세요 >> ')

# # print('번호\t이름')
# for i in range(len(member)):
#     # print(i)
#     for j in range(len(member[i])):
#         # print(j)
#         if search2 in member[i]:
#             del(member[i])
#             print('{}\t{}'.format(member[i][0],search2))
#             print('학생이 삭제되었습니다.')