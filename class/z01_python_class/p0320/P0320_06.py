# input 입력받은 데이터를
# p0320.txt 파일을 생성해서 저장하시오.
# p_0320은 현재날자를 사용하시오.

import datetime

now = datetime.datetime.now()
file_name = now.strftime('p_%m%d')

print(file_name)


with open(f'{file_name}','w',encoding='utf8') as f:
    while True:
        a = input('메모장 >>(0.취소)')
        txt = f.write(a+'\n')
        if a == '0':
            print('메모장 종료')
            break
        
