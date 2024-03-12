students = {'stuNo':1,'stuName':'홍길동','kor':100}
students['eng'] = 100  # 딕셔너리 추가
students['kor'] = 50   # 딕셔너리 수정
del students['stuName']  # 딕셔너리 삭제
print(students)

# 타입 list, dict, int, str, float  으로 형변환  중요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(list(students.keys())) # 딕셔너리의 키 값을 리스트로 추출
print(students.values()) # 딕셔너리의 value 값만 출력
print(students.items()) # key, value 를 토플 형태로 출력
# 토플은 수정 삭제가 불가능!! 하려면 형타입 변환

print(sorted(students))


list = [1,2,3]
list.append(4)
del list[0]
list[0] = 100
print(list)
list.remove(3)
print(list)
# list[3] = 1000   에러. 없는 공간
print(list)



