students = [{'stuNo': 's001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
            {'stuNo': 's002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
            {'stuNo': 's003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
            {'stuNo': 's004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
            {'stuNo': 's005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

# 학생성적 입력부분 구현하세요
stu_cnt = len(students)

while True:
    student = {}
    stu_name = input('입력할 학생의 이름을 입력하세요. (0. 취소)>>  ')
    if stu_name == '0':
        break
    stu_kor = int(input('국어점수를 입력하세요 >>   '))
    stu_eng = int(input('영어점수를 입력하세요 >>   '))
    stu_math = int(input('수학점수를 입력하세요 >>   '))
    stu_total = stu_kor + stu_eng + stu_math
    stu_avg = stu_total / 3
    student['stuNo'] = 's{:03d}'.format(stu_cnt + 1)
    student['name'] = stu_name
    student['kor'] = stu_kor
    student['eng'] = stu_eng
    student['math'] = stu_math
    student['total'] = stu_total
    student['avg'] = stu_avg
    stu_cnt += 1
    students.append(student)
    
    print(students)
    
    
# 학생성적 출력부분 구현하세요
while True:
    print_choice = input('학생성적을 전체출력하시겠습니까?(1.출력 / 0.취소)')
    if print_choice == '0':
        break
    elif print_choice == '1':
        print('='*60)
        print('학번\t이름\t국어\t영어\t수학\t총점\t평균')
        print('-'*60)
        for i in students:
            for j in i:
                print(i[j],end = '\t')
            print()
        # for i in students:     >>> 이것도 가능함 (for문을 한번만 써서)
        # print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(i['stuNo'],i['name'],i['kor'],i['eng'],i['math'],i['total'],i['avg']))
        print('='*60)
    else : 
        print('번호를 다시 입력하세요.')
