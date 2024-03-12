member = []

# 입력 : 이름, 점수
# 총 3명의 정보를 member리스트에 넣으세요

# for i in range(3):
#     a = input('이름을 입력하세요 >')
#     b = int(input('점수를 입력하세요 >'))
#     mem = [a, b]                      # append 사용 가능
#     member.append(mem)

member = [['홍길동',55], ['유관순',80], ['이순신',90]]
print(member) 

#60점 이상이면 홍길동님 불합격입니다. 유관순님 합격입니다.
for i in range(len(member)):
    if member[i][1] >= 60 :
        print('{}님 합격입니다.'.format(member[i][0]))
    else :
        print('{}님 불합격입니다.'.format(member[i][0]))

import datetime
now = datetime.datetime.now()
from random import *

print(int(random()*10))