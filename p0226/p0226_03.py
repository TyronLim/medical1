# list
# 데이터를 잘 관리하기 위해서 묶어서 관리하는 자료형
# 리스트 변수명 = [요소1, 요소2, 요소3, 요소4 ......]
lis1 = []
lis2 = [0,2,4]
lis3 = ['짝수', '홀수']
lis4 = ['홍길동', 100, 100, 100]
lis5 = ['짝수', [2,4,6], '홀수', [1,3,5]] # 리스트 안에 리스트 사용 가능

# 인덱싱 (index) 리스트를 검색, 접근
# index는 0부터 시작
numL = [0,1,2,3,4]
print(numL[0])
print(numL[-5]) # 리스트 안의 '0' 출력

# 인덱스의 범위를 넘어가면 오류 출력 (numL[10]를 프린트하면 오류)

# 인덱스를 가지고 리스트의 특정 요소의 값을 수정 할 수 있다.
# 리스트명[n] = 값
numL[0] = 20
print(numL)
numL[-1] = 222
print(numL)

# lis5 = ['짝수', [2,4,6], '홀수', [1,3,5]]
# 숫자2에 접근하기 위해서는?

print(lis5[1]) #[2,4,6]
print(lis5[1][0]) # 2에 접근
print(lis5[3][2]) # 5에 접근
print(lis5[-1][-1]) # 5에 접근

# 리스트 슬라이싱 : 리스트자르기
# 콜론 : 를 사용해서 ~부터 ~까지
# 리스트명[시작인덱스 : 끝 인덱스+1]
numL = [0,1,2,3,4]
print(numL[2:4]) # 2이상 4미만
print(numL[1:]) # 1번부터 끝까지
print(numL[:3]) #처음부터 3번미만까지
print(numL[0:0]) # 

#리스트의 길이 : len(리스트명)
print(len(numL))
print(len(lis5))

# 특정 요소 삭제: del(리스트명)
aa = [100,200,300,400,500,600,700]
print(aa)
del(aa[1])
print(aa)
del(aa[1:3])
print(aa)

# 리스트 값 추가 : 리스트명.append(값)
aa = [100,200,300,400,500,600,700]
aa.append(800)
print(aa)
aa.append('숫자')
aa.append([1,2,3])
print(aa)

# 리스트에서 특정값 제거
# 리스트명.remove(값)
aa.remove(200)
print(aa)

aa.append(100)
aa.append(400)
aa.append(100)
print(aa)
aa.remove(100) #같은 값이 두 개 이상일 땐 제일 첫번때 값만 삭제. 뒤의 100은 유지.
print(aa)

# aa.remove(1) # 1이 없으므로 오류

# 요소확인 : 내부 포함된 요소의 존재를 확인하는 방법
# in, not in
print(100 in aa)
print(800 not in aa)
print(2 in aa)

f = ['사과', '딸기', '복숭아', '수박', '배']
print('딸기' in f)

if '사과' in f:
    print('사과가 있습니다.')
else :
    print('사과가 없습니다.')
    
if '사과' not in f:
    print('사과가 없습니다')
else :
    print('사과가 있습니다')


