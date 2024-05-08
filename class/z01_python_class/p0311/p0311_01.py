students = [{'stuNo': 's001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
            {'stuNo': 's002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
            {'stuNo': 's003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
            {'stuNo': 's004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
            {'stuNo': 's005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

stu_cnt = len(students)

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
        print('숫자만 입력가능합니다. 다시 입력해주세요.')
        continue   # 반복문 다시 처음부터 실행
    choice = int(choice)
    
    if choice == 1:
        print('학생성적입력을 선택하셨습니다.')
        while True:
            student = {}
            name = input('학생의 이름을 입력해주세요 (0. 취소) >> ')
            if name == '0':
                break
            
            kor = int(input('국어 점수를 입력해주세요 >>'))
            eng = int(input('영어 점수를 입력해주세요 >>'))
            math = int(input('수학 점수를 입력해주세요 >>'))
            total = kor + eng + math
            avg = total / 3
            
            student['stuNo'] = 's{:03d}'.format(stu_cnt+1)
            student['name'] = name
            student['kor'] = kor
            student['eng'] = eng
            student['math'] = math
            student['total'] = total
            student['avg'] = avg
            students.append(student)
            
            print(f'{name}학생이 입력되었습니다.')
            print(students[stu_cnt])
            stu_cnt += 1
    
    elif choice == 2:
        choice_print = input('학생성적전체출력을 선택하셨습니다.(1. 출력 / 0, 취소)')
        if not choice_print.isdigit():
            print('올바른 번호를 입력해주세요. (1. 출력 / 0, 취소)')
            continue
        choice_print = int(choice_print)
        
        while True:
            if choice_print == 0:
                print('학생성적전체출력을 취소하셨습니다.')
                break
            
            elif choice_print == 1:
                print('학번\t이름\t국어\t영어\t수학\t총합\t평균')
                for stu in students:
                    print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                        stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg']))
                break
                
    elif choice == 3:
        print('학생검색을 선택하셨습니다.')
        while True:
            choice_search = input('검색할 학생의 이름을 입력해주세요.(0.취소) >> ')
            if choice_search == '0':
                break
            
            cnt = 0
            for stu in students:
                if choice_search == stu['name']:
                    print(f'입력하신 {choice_search}학생의 성적을 찾았습니다.')
                    print('학번\t이름\t국어\t영어\t수학\t총합\t평균')
                    print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                        stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg']))
                    cnt += 1
                
            if cnt == 0:
                print(f'입력하신 {choice_search}학생의 정보가 없습니다.')

    
    
    elif choice == 4:
        print('학생수정을 선택하셨습니다.')
        cnt = 0
        while True:
            choice_change = input('수정할 학생의 이름을 입력하세요 (0. 취소)>> ')
            if choice_change == '0':
                print('학생수정을 취소하셨습니다.')
                break
                        
            for stu in students:
                if choice_change == stu['name']:
                    print('입력하신 {}학생의 정보입니다.'.format(choice_change))
                    print('학번\t이름\t국어\t영어\t수학\t총합\t평균')
                    print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                        stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg']))
                    
                    while True:
                        stu_change = input('변경하실 항목을 선택해주세요.(1.이름 / 2.국어 / 3.영어 / 4.수학 / 0.취소)')
                        if not stu_change.isdigit():
                            print('올바른 항목을 입력해주세요.') 
                            break
                        stu_change = int(stu_change)
                       
                        if stu_change == 1:
                            change = input('변경할 이름을 입력해주세요.>> ')
                            stu['name'] = change
                            print('이름이 {}로 변경되었습니다.'.format(stu['name']))
                            print('학번\t이름\t국어\t영어\t수학\t총합\t평균')
                            print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                                stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg']))
                            cnt = 1

                        elif stu_change == 2:
                            change = input('국어 점수를 입력해주세요.>> ')
                            if not change.isdigit():
                                print('올바른 점수(숫자)를 입력해주세요.')
                                break
                            change = int(change)
                            stu['kor'] = change
                            stu['total'] = stu['kor']+stu['eng']+stu['math']
                            stu['avg'] = stu['total'] / 3
                            print('{}학생의 국어 점수가 변경되었습니다.'.format(stu['name']))
                            print('학번\t이름\t국어\t영어\t수학\t총합\t평균')
                            print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                                stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg']))
                            cnt = 1
                            
                        elif stu_change == 3:
                            change = input('영어 점수를 입력해주세요.>> ')
                            if not change.isdigit():
                                print('올바른 점수(숫자)를 입력해주세요.')
                                break
                            change = int(change)
                            stu['eng'] = change
                            stu['total'] = stu['kor']+stu['eng']+stu['math']
                            stu['avg'] = stu['total'] / 3
                            print('{}학생의 영어 점수가 변경되었습니다.'.format(stu['name']))
                            print('학번\t이름\t국어\t영어\t수학\t총합\t평균')
                            print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                                stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg']))
                            cnt = 1
                            
                        elif stu_change == 4:
                            change = input('수학 점수를 입력해주세요.>> ')
                            if not change.isdigit():
                                print('올바른 점수(숫자)를 입력해주세요.')
                                break
                            change = int(change)
                            stu['math'] = change
                            stu['total'] = stu['kor']+stu['eng']+stu['math']
                            stu['avg'] = stu['total'] / 3
                            print('{}학생의 수학 점수가 변경되었습니다.'.format(stu['name']))
                            print('학번\t이름\t국어\t영어\t수학\t총합\t평균')
                            print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                                stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg']))
                            cnt = 1
                        
                        elif stu_change == 0:
                            print('{}학생에 대한 수정을 취소합니다.'.format(choice_change))
                            break
                        
            if cnt == 0:
                print('입력하신 {}학생에 대한 정보가 없습니다.'.format(choice_change))
                        
    elif choice == 5:
        while True:
            choice_rank = input('등수처리를 실행하시겠습니까?(1.실행 / 0.취소)')
            if choice_rank == '0':
                break
            
            elif choice_rank == '1':
                for i in students:
                    rank_cnt = 1
                    for j in students:
                        if i['total'] < j['total']:
                            rank_cnt += 1
                    
                    i['rank'] = rank_cnt
                print('등수처리가 완료되었습니다.')  
                print(students)
                break
                
            else :
                print('올바른 번호를 입력해주세요.(1.실행 / 0.취소)')
                        
    elif choice == 6:
        print('학생삭제를 선택하셨습니다.')
        while True:
            cnt = 0
            stu_del = input('삭제할 학생의 이름을 입력해주세요.(0.취소)>> ')
            if stu_del == '0':
                print('학생 삭제를 취소합니다.')
                break
            
            for stu in students:
                if stu_del == stu['name']:
                    break
                cnt += 1
            print('찾고자 하는 학생의 위치는 {}입니다.'.format(cnt))
                
            if cnt >= len(students):
                print('찾고자 하는 학생이 없습니다.')
            
            else : 
                s_input = input('학생을 삭제하시겠습니까?(0.취소 / 1.삭제)')
                if s_input == '0':
                    break
                
                elif s_input == '1':
                    del(students[cnt])
                    print('{}학생이 삭제되었습니다.'.format(stu_del))
                
                else :
                    print('올바른 번호를 입력해주세요.(0.취소 / 1.삭제)')

        
    elif choice == 0:
        break
            
            
            
            
            
            
            
    