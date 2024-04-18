# 빈 리스트 생성
# cont = []
# cont2 = ['미','중','러','일']
# c1 = input('1.나라를 입력해 주세요 >> ')
# c2 = input('2.나라를 입력해 주세요 >> ')
# c3 = input('3.나라를 입력해 주세요 >> ')
# c4 = input('4.나라를 입력해 주세요 >> ')

# cont.append (c1)
# cont.append (c2)
# cont.append (c3)
# cont.append (c4)

# # print(cont)

# print(cont2)
# print('{}-{}-{}-{}'.format(cont[0],cont[1],cont[2],cont[3]))
# print('%s-%s-%s-%s'%(c1,c2,c3,c4))

f= ['샤인머스켓', '딸기', '수박', '귤', '바나나', '키위', '망고']

f1 = []

f1.append(input('1번 과일 이름을 입력하세요 >>'))
f1.append(input('2번 과일 이름을 입력하세요 >>'))
f1.append(input('3번 과일 이름을 입력하세요 >>'))

print('내가 좋아하는 과일은 {}, {}, {}입니다.'.format(f1[0],f1[1],f1[2]))

f2 = []
a = (input('1번 과일 이름을 입력하세요 >>'))
b = (input('2번 과일 이름을 입력하세요 >>'))
c = (input('3번 과일 이름을 입력하세요 >>'))

f2.append(a)
f2.append(b)
f2.append(c)

print('제가 좋아하는 과일은 {},{},{}입니다'.format(f2[0],f2[1],f2[2]))