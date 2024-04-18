# 입력 : 이름, 아이디, 비밀번호
# 5명을 입력받아서 member 리스트를 만드세요

'''
member리스트
이름    아이디  비밀번호
홍길동   aaa      1111
유관순   bbb      2222
'''
member = [] # [[홍길동, aaaa, 1111],[유관순, bbbb, 2222]]

for i in range(5):
    name = input('이름 >')
    id = input('아이디 >')
    pas = input('비밀번호 >')
    mem = []
    mem.append(name)
    mem.append(id)
    mem.append(pas)
    member.append(mem)

print('='*25)
print('이름\t아이디\t비밀번호')
print('-'*25)
for i in range(len(member)):
    print('{}\t{}\t{}'.format(member[i][0],member[i][1],member[i][2]))
print('='*25)
# for i in range(len(member)):
#     print(member[i][0],'\t',member[i][1],'\t',member[i][2])
    


