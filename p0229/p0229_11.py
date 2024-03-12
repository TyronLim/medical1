fruits = [['딸기','사과'],'자몽','포도','수박','자몽']

# 자몽을 삭제  > fruits.remove('자몽')  > 제일 앞에 있는 자몽이 삭제가 됨

# del(fruits[5])
# print(fruits)
# 지정해서 삭제 가능

for i in range(len(fruits)):
    for k in range(fruits[i]):
        print(k)

# for j in fruits:
#     # print(j)
#     for n in range(len(j)):
#         print(n)
