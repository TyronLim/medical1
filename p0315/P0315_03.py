import P0315_02

member = P0315_02.idpw()

# mem.txt 파일에 aaa,1111이라는 문자를 저장하시오.

f = open('mem.txt','w',encoding = 'utf-8')

for i in member:
    f.write(f'{i[0]},{i[1]}\n')

f.close()




