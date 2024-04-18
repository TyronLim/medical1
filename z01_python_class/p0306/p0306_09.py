students = [{'stuNo': 's001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
            {'stuNo': 's002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
            {'stuNo': 's003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
            {'stuNo': 's004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
            {'stuNo': 's005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

# 모든 학생의 국어 점수를 출력하시오.
for j, i in enumerate(students):
    print(f'{j}. {i['name']} : {i['kor']}')
















# print(students[1]['name'])
# print(students[4]['name'])

# print(students[3]['kor']+students[3]['eng'])

# students[2]['kor'] = 100
# print(students[2])

# print(len(students[0]))

# for i,j in enumerate(students):
#     print(f'{i+1}. {j['name']}',end = ' ')

# print()

# for i, j in enumerate(students[0]):
#     print(i)
#     # print(j)


