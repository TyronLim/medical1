# 학번 1000, 이름 홍길동, 학과 컴퓨터공학      딕셔너리

student = {'학번':1000, '이름': '홍길동', '학과':'컴퓨터공학'}

for key in student:
    print('{}:{}'.format(key, student[key]))

    
print('-'*40)



print(student['학번'])

# 추가 : 연락처 010-1111-1111
student['연락처'] = '010-1111-1111'

print(student)

# 수정
student['이름'] = '유관순'
print(student)

# 수정2 학과 > 화학과
student['학과'] = '화학'
print(student)

print(student.get('이름'))   # 출력 방법
print(student['이름'])       # 같은 방법


# print(student['성별'])       # key값이 없을 때 에러
print(student.get('성별'))     # key값이 없을 때 none 

if '이름' in student:
    print('이름 키값 있음')
    print('이름 : ',student['이름'])
else :
    print('이름 키값 없음')


if '성별' in student:
    print('성별 키값 있음')
    print('성별 : ',student['성별'])
else :
    print('성별 키값 없음')
    
    
for i in student.keys():
    print(i)
# student.keys() 딕셔너리의 모든 key를 출력
print(type(student.keys()))   
print(student.keys())
print(list(student.keys())) # 형변환을 해야 list 타입으로 변환됨

print('-'*50)

# student.values() 딕셔너리의 모든 value를 출력
print(student.values())
print(list(student.values()))
for i in student.values():
    print(i)
    
# items () 튜플 형태 데이터를 리턴
print(student.items())

if '이름' in student.items():
    print('키 값이 있습니다.')
else:
    print('키 값이 없습니다.')
    