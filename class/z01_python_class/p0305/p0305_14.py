import operator

numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
counter = {}
# counter[1] = 2
# counter[2] = 1
# print(counter)

for number in numbers:
    if number not in counter:   # counter 딕셔너리에 키값이 없으면
        counter[number] = 0     # 딕셔너리에 키 값 0을 추가
    
    counter[number] += 1        # 딕셔너리(0)에 1을 증가
    
print(counter)

print(sorted(counter.items(),key=operator.itemgetter(1)))
    

        
    
    
    
      
