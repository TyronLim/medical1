# 리스트변수명 = [요소1,요소2, ... 요소n]
# 요소가 될 수 있는 타입 : bool, int, float, string, list

fruits = ['딸기','사과','배','수박','귤']

print(fruits[4])
print(fruits[-1])
print(fruits[len(fruits)-1])
# 리스트에 요소를 추가
fruits.append('포도')
print(fruits)
fruits.remove('딸기')  # 특정 요소를 삭제
print(fruits)
# 리스트에서 3번째꺼 삭제하고 싶을 때
del(fruits[3])
print(fruits)

if '한라봉' in fruits:
    print('있음')

for f in fruits:
    print(f)
    
for i in range(len(fruits)):
    print(fruits[i])
    
num = [[10,20,30],[100,200,300],[1,2,3]]
for n in num :
    print(n)
for n in num :
    for a in n :
        print(a)
        
for i in range(len(num)):
    for j in num[i]:
        print(j)
        
for j in range(len(num)):
    for i in range(len(num[j])):
        print(num[j][i])

# 리스트에 숫자 넣을 떄 한 줄로 표현하기

aa = []
for i in range(1,11):
    aa.append(i)
print(aa)
# [표현식 for 항목 in 리스트 if 조건문]
# a = [i for i in range(1,11)]
# b = [0 for i in range(10)]    # >> 0이 10개 들어감
# c = [0 for i in range(3,14)]   # >> 0이 11개 들어감
# d = [[] for i in range(10)]   # >> 리스트가 10개 들어감
# print(a)
# print(b)
# print(c)

# e = [i*j for i in range(1,3) for j in range(1,3)]
# print(e)

# f = [i for i in range(100) if i%2 == 0]
# print(f)

# g = [i for i in range(1,11)]
# print(g)
# h = [i+1 for i in g]
# print(h)

names = ['홍길동','유관순','이순신','강감찬','김구']

for i in range(len(names)):
    print('{}.{}'.format(i+1,names[i]))

#변수 1개 더 필요
a = 0
for i in names:
    a+=1
    print('{}.{}'.format(a,i))
    
# enumerate 함수
# index를 넣고 싶을 때 사용
for i, name in enumerate(names):
    print('{}는 {}번째에 있습니다.'.format(name, i+1 ))
    