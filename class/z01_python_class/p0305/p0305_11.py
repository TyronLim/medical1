students = []

# 학번, 이름, 국어, 영어, 수학, 합계, 평균   입력하는 프로그램
# 학번 = K0001, K0002 ...
num= 0
while True:
    chk = input('학생 성적을 추가하시겠습니까?(1.추가 , 0,취소)>> ')
    if chk == '1':
        student = {}                                        # 딕셔너리
        num += 1
        stuNo = ('K{:04d}'.format(num))               # 학번 생성
        
        name = input('이름을 입력하세요 >> ')
        kor = int(input('국어점수를 입력하세요 >> '))
        eng = int(input('영어점수를 입력하세요 >> '))
        math = int(input('수학점수를 입력하세요 >> '))
        total = kor + eng + math
        avg = '{:.2f}'.format(total / 3)
        student['stuNo'] = stuNo                          # 학번 추가
        student['name'] = name                            # 이름 추가
        student['kor'] = kor                              # 국어 추가
        student['eng'] = eng                              # 영어 추가
        student['math'] = math                            # 수학 추가
        student['total'] = total                          # 합계 추가
        student['avg'] = avg                              # 평균 추가
       
        students.append(student)                            # student 를 studests 에 추가
        
        print('[학생정보내역]')
        for k in student.keys():
            print('{} : {}'.format(k,student[k]))
        print('-'*40)
        print('학생 1명이 추가되었습니다.')
        
    else : 
        print('학생 성적을 종료합니다.')
        break

print(student)


# stuNo = 1
# name = input('이름을 입력하세요')
