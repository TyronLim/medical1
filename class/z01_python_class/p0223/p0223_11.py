# 리스트
# 1도 기억하고, 2도 기억하고 싶을 때.
# 대괄호로 감싸서 나타내며, 0개 이상의 원소가 저장될 수 있습니다.
num = 1
num = 2
print(num) #하면 2로 출력된다.

listA = [1,2]
listB = []

n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5

list1 = [1,2,3,4,5]
list2 = ['사과', '복숭아', '딸기', '배', '포도', '수박']   # 0,1,2,3,4,5 순으로 지정
list3 = [1, '홍길동', 99.1] # 파이썬은 여러 형태의 변수를 섞어서 사용 가능

print(list2[1])
print(list1[3])
print(list3[2])
print(list2[-2])  # 마이너스는 뒤에서부터 -1,-2,-3,-4 순으로

#리스트의 길이 출력
a=len(list2)
print(a)
print(len(list2))

#list2에서 딸기 출력하기
print(list2[2])
print(list2[-4])

ho = [1,2,3,4,5,6,7]
print(ho[-2])
print(ho[len(ho)-6])

# 리스트 슬라이싱
aa = [0,1,2,3,4,5,6,7,8,9,10]

print(aa[1:4]) # 1 이상, 4 미만 [1,2,3] 출력
print(aa[3:8]) # [3,4,5,6,7]
print(aa[2:]) # 2번부터 끝까지 [2,3,4,5,6,7,8,9,10]
print(aa[:7]) # 처음부터 7미만까지 [0,1,2,3,4,5,6]
print(aa[:]) # 처음부터 끝까지
print(aa[1:-1]) # 1번부터 제일끝미만 까지 [1,2,3,4,5,6,7,8,9]

# 요소확인 : 내부에 포함되어 있는지 확인하는 방법을 제공해줌
# in, not in
print('포도'in list2)
print(11 in aa)
print(0 not in aa)

listC = [1,2,3,['a','b','c'],[4,5]]

print(listC[3])
print(listC[4])
print(1 in listC)
print(4 in listC)
print([4,5] in listC)

