import operator

fruits = ['바나나', '바나나',
           '바나나', '딸기', '배', '사과', '딸기',
            '딸기', '딸기', '딸기', '사과','바나나', '바나나',
           '바나나', '딸기', '배', '사과', '딸기',
            '딸기', '딸기', '딸기', '사과']
counter = {}

for i in fruits:
    if i not in counter:
        counter[i] = 0
    
    counter[i] += 1

print(counter)                              # 그냥 출력
print(sorted(counter.items(),key = operator.itemgetter(1),reverse = True))    # value 내림차순 출력
print(list(counter))                        # key 그냥 출력
print(sorted(counter.keys()))               # key 정렬 출력
print(list(counter.values()))               # value 그냥 출력
print(sorted(counter.values()))             # value 정렬 출력
print(counter.get('딸기'))





