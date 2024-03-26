students = [[1,'홍길동',100,100,100,300,100],
            [2,'유관순',90,90,90,270,90],
            [3,'이순신',80,80,80,240,80]]

while True:
    search = input('찾는 학생의 이름을 입력하세요. >> ')
    chk = 0
    count = 0
    for stu in students:
        if search in stu:
            chk = 1
            break
        count += 1               # 찾는 학생의 위치값
    
    if chk == 0:
        print('찾는 학생의 정보가 없습니다.')
    else:
        print('입력한 학생{}을 찾았습니다.'.format(search))
        print('변경할 과목 선택')
        num = int(input('1. 국어점수변경  2. 영어점수변경 3. 수학점수변경 0. 취소  >  '))
        print('-'*20)
        if num == 1:
            print('국어를 선택하셨습니다.')
            print('현재 국어점수는 {}입니다.'.format(students[count][2]))
            kor = int(input('변경할 점수를 입력하세요 >> '))
            students[count][2] = kor
            # 합계, 평균도 넣어야 함.
            total = students[count][2]+students[count][3]+students[count][4]
            avg = total / 3
            students[count][5] = total
            students[count][6] = float('{:.2f}'.format(avg))
            
            print(students)
            # 성적수정 프로그램 구현
            
        elif num == 2:
            print('영어를 선택하셨습니다.')
            print('현재 영어점수는 {}입니다.'.format(students[count][3]))
            eng = int(input('변경할 점수를 입력하세요 >> '))
            students[count][3] = eng
            # 합계, 평균도 넣어야 함.
            total = students[count][2]+students[count][3]+students[count][4]
            avg = total / 3
            students[count][5] = total
            students[count][6] = float('{:.2f}'.format(avg))
            
            print(students)
            
        elif num == 3:
            print('수학을 선택하셨습니다.')
            print('현재 수학점수는 {}입니다.'.format(students[count][4]))
            math = int(input('변경할 점수를 입력하세요 >> '))
            students[count][4] = math
            # 합계, 평균도 넣어야 함.
            total = students[count][2]+students[count][3]+students[count][4]
            avg = total / 3
            students[count][5] = total
            students[count][6] = float('{:.2f}'.format(avg))
            
        elif num == 0:
            print('종료됩니다.')
            break