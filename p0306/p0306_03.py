import operator
# numbers에 있는 숫자들이 몇번 나왔는지 
# 딕셔너리로 출력하시오.
numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
counter = {}

for n in numbers:
    if n not in counter:
        counter[n] = 0
    counter[n]+=1

print(counter)

array = ['F','D','A','C','A','C','F','B','C','E']
counter2 = {}

for a in array:
    if a not in counter2:
        counter2[a] = 0
    counter2[a] += 1
    
print(counter2)

print(sorted(counter.items(),key=operator.itemgetter(0)))
print(sorted(counter2.items(),key=operator.itemgetter(0)))

t_dic = {'peach':'복숭아', 'orange':'오렌지', 'apple':'사과',
         'pear':'배', 'grapes':'포도', 'mango':'망고','kiwi':'키위'}

