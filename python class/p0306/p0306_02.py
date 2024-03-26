import operator

fruits = ['바나나', '바나나',
          '바나나', '딸기', '배', '사과', '딸기',
          '딸기', '딸기', '딸기', '사과','바나나', '바나나',
          '바나나', '딸기', '배', '사과', '딸기',
          '딸기', '딸기', '딸기', '사과']
counter = {}  # 딕셔너리 생성

for f in fruits:
    if f not in counter:
        counter[f] = 0
        
    counter[f] += 1
        
print(counter)

print(counter.get.values())

# 딕셔너리 정렬 key값 순으로 정렬
# print(sorted(counter.items(),key=operator.itemgetter(0)))   # key 오름차순
# print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True))  # key 내림차순
# print(sorted(counter.items(),key=operator.itemgetter(1)))   # value 오름차순
# print(sorted(counter.items(),key=operator.itemgetter(1),reverse=True))  # value 내림차순
