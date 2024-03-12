students = [] # 학생 성적 저장
students = [[1, '홍길동', 100, 100, 100, 300, 100.00, 0],
            [2, '유관순', 100, 100, 100, 300, 100.00, 0],
            [3, '이순신', 90, 90, 90, 270, 90.00, 0],
            [4, '김구', 90, 80, 70, 240, 80.00, 0],
            [5, '김유신', 70, 60, 90, 220, 73.33, 0]]
cnt = len(students) # 학번
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요 >> ')
    if not choice.isdigit():
        print('숫자만 입력가능합니다.')
        continue   # 반복문 다시 처음부터 실행
    choice = int(choice)
    
    # 1. 학생성적입력 프로그램
    if choice == 1:
        chk = 0
        while True:   # 무한 반복
            print('학생성적을 입력합니다.')
            student = []
            name = input('이름 입력 (0. 취소)>> ')
            # name.isdigit()
            if name == '0':
                break
            cnt = cnt+1 # 학번
            student.append(cnt)
            student.append(name)
            student.append(int(input('국어 성적 >> ')))
            student.append(int(input('영어 성적 >> ')))
            student.append(int(input('수학 성적 >> ')))
            sum = student[2]+student[3]+student[4]   # 합계 저장
            student.append(sum)
            avg = sum/3                              # 평균 저장
            student.append(float('{:.2f}'.format(avg)))
            student.append(0)
            students.append(student)
            print(students)

        
                # 2. 학생성적출력 프로그램
    elif choice == 2 :
        # 전체학생출력
        print('[학생성적출력]')
        print('-'*50)
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
        print('-'*50)
        # 2차원 리스트 for문 2번 사용
        for stu in students:    
            for i in stu:
                print(i,end='\t')
            print()
        print('-'*30)

        # 3. 학생검색 프로그램
    elif choice == 3 :
        while True:
            search = input('검색하고 싶은 학생 이름을 입력하세요.(종료는 0번)>>')   # 학생 입력   
            chk = 0    # 찾는 정보 확인
            count = 0
            if search == 0:
                break
            for stu in students:                                   # 학생 찾기
                if search in stu:
                    chk = 1
                    break
                count += 1
                    # if stu[1] == search:
                    #     print('{}의 학생정보를 찾았습니다.'.format(search))
            
            if chk == 1 :
                print('{}의 학생정보를 찾았습니다.'.format(search))
                print('[학생성적출력]')
                print('-'*50)
                print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
                print('-'*50)
                for i in students[count]:
                    print(i,end= '\t')
                print()
                                    
            else:
                print('찾는 학생정보가 없습니다.')
                break
            
    # 4. 학생수정 프로그램 
    elif choice == 4:
        while True:
            search = input('찾는 학생의 이름을 입력하세요. >> ')
            chk = 0                 # 있으면 1, 없으면 0 그대로.
            count = 0  
            if search == '0':
                print('수정이 종료됩니다.')
                break    
               
            for stu in students:
                if search in stu:
                    chk = 1
                    break
                count += 1               # 찾는 학생의 위치값
            
            if chk == 0:
                print('찾는 학생의 정보가 없습니다.')
            else:                   #chk = 1
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
                    print('국어점수가 변경되었습니다.')
                    total = students[count][2]+students[count][3]+students[count][4]
                    avg = total / 3
                    students[count][5] = total
                    students[count][6] = float('{:.2f}'.format(avg))
                    
                
                elif num == 2:
                    print('영어를 선택하셨습니다.')
                    print('현재 영어점수는 {}입니다.'.format(students[count][3]))
                    eng = int(input('변경할 점수를 입력하세요 >> '))
                    students[count][3] = eng
                    # 합계, 평균도 넣어야 함.
                    print('영어점수가 변경되었습니다.')
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
                    print('수학점수가 변경되었습니다.')
                    total = students[count][2]+students[count][3]+students[count][4]
                    avg = total / 3
                    students[count][5] = total
                    students[count][6] = float('{:.2f}'.format(avg))
                    
            if search == 0:
                print('수정이 종료됩니다.')
                break    
                    
    elif choice == 5:
        while True:
            choice = input('등수처리를 실행하시겠습니다?(1.실행 , 2.취소)')
            if choice == '2':
                print('등수처리를 취소하셨습니다.')
                break
            elif choice == '1':
                print('등수처리를 선택하셨습니다.')
                for i_stu in students:
                    no = 1              # 등수 초기화
                    for j_stu in students:
                        # 각각의 총합 비교
                        if i_stu[5] < j_stu[5]:
                            no += 1    # 비교대상 총합이 더 크면 1 증가
                    i_stu[7] = no       # 등수를 students에 있는 등수 자리에 입력
            print('등수처리가 완료되었습니다.')
            print('-'*40)
            print(students)
                    
    # 학생 삭제  
    elif choice == 6:
        while True:
            search = input('삭제하려는 학생을 입력하세요.(취소 = 0)')
            if search == '0':
                break
            cnt = 0 # 찾은 학생의 위치
            for i,stu in enumerate(students):                 # 이름 찾기(for문)
                if stu[1] == search:
                    break
                cnt += 1
                    
            if cnt == len(students):
                print('{}학생에 대한 정보가 없습니다.'.format(search))
                
            else :
                print('{}학생에 대한 정보가 있습니다.'.format(search))
                real = int(input('정말 삭제하시겠습니까? (1 / 2)'))
                if real == 1:
                    del students[cnt]
                elif real != 2:
                    print('삭제가 취소되었습니다.')
                    break
                else :
                    print('잘못입력하셨습니다.')
                
            print(students)

            
    # 0. 프로그램 종료
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break # 반복문 종료
