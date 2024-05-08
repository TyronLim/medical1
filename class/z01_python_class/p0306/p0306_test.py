students = [{'stuNo': 's001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33, 'rank': 0}, 
            {'stuNo': 's002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67, 'rank': 0}, 
            {'stuNo': 's003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67, 'rank': 0}, 
            {'stuNo': 's004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0, 'rank': 0}, 
            {'stuNo': 's005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67, 'rank': 0}]

stu_no = len(students)

while True:
    print('[학생성정프로그램]')
    print('-'*40)
    print('[1. 학생성적입력]')
    print('[2. 학생성적전체출력]')
    print('[3. 학생성적검색출력]')
    print('[4. 학생성적수정]')
    print('[5. 학생성적삭제]')
    print('[6. 등수처리]')
    print('[0. 프로그램 종료]')
    choice = input('실행할 목록을 선택하세요. >> ')
    
    if choice.isdigit():
        choice = int(choice)
    
    if choice == 1:    # 학생성적입력
        while True:
            student = {}
            print('학생성적입력을 선택하셨습니다. ')
            name = input('입력할 학생의 이름을 입력하세요. (0. 뒤로가기) >> ')
            
            if name == '0':
                print('학생입력을 종료하셨습니다.')
                break
            kor = int(input('국어점수를 입력하세요 >> '))
            eng = int(input('영어점수를 입력하세요 >> '))
            math = int(input('수학점수를 입력하세요 >> '))
            total = kor + eng + math
            avg = total/3
            rank = 0
            student['stuNo'] = 's'+'{:03d}'.format(stu_no)
            student['name'] = name
            student['kor'] = kor
            student['eng'] = eng
            student['math'] = math
            student['total'] = total
            student['avg'] = avg
            student['rank'] = rank
            students.append(student)
            print('{}학생이 추가되었습니다.'.format(name))
            print(students)
            print('-'*50)
    
    elif choice == 2:  # 학생성적전체출력
        print('학생성적전체출력을 선택하셨습니다.')
        while True:
            choice_print = input('학생성적전체출력을 실행하시겠습니까?(0.실행 / 1.취소) >> ')
            if choice_print == 1:
                break
            elif choice_print == 0:
                print('='*50)
                print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                print('-'*50)
                for stu in students:
                    for i in stu:
                        print(stu[i],end='\t')
                    print()
            else :
                print('번호를 다시 입력하세요')
    
    elif choice == 3:
        print('학생성적 검색출력을 선택하셨습니다.')
        
        while True:
            exist = 0     # 0 없음, 1 있음
            search_name = input('검색할 학생의 이름을 입력하세요.(0.취소) >> ')
            if search_name == '0':
                print('학생 검색이 종료되었습니다.')
                break
            
            for stu in students:
                if search_name in stu['name']:  
                    print(f'{search_name}학생이 존재합니다')
                    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                            stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg'],stu['rank']))
                    exist = 1
                    
            if exist == 0: 
                print('학생 정보가 존재하지 않습니다.')

    elif choice == 4: ## 다음 꺼
        print('학생성적수정을 선택하셨습니다.')
        chk = 0
        while True:
            search = input('검색할 학생의 이름을 입력해주세요. (0.취소)>> ')
            for stu in students:
                    if search not in stu['name']:
                        print('{}학생에 대한 정보가 없습니다'.format(search))
                
                    elif search in stu:
                        print('{}학생이 검색되었습니다.'.format(search))
                        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                                    stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg'],stu['rank']))
                        change = int(print('수정할 항목을 선택해주세요.(1. 이름, 2. 국어, 3. 영어, 4. 수학)>> '))
                        
                        if change == 1:
                            ch_info = input('수정할 이름을 입력해주세요 >> ')
                            stu['name'] = ch_info
                            print('이름이 수정되었습니다.')
                            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                                    stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg'],stu['rank']))
                        
                        elif change == 2:
                            ch_info = int(input('수정할 국어점수를 입력하세요. >> ')) 
                            stu['kor'] = ch_info
                            stu['total'] = stu['kor'] + stu['eng'] + stu['math']
                            stu['avg'] = stu['total'] / 3
                            print('국어점수가 수정되었습니다.')
                            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                                    stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg'],stu['rank']))
                        
                        elif change == 3:
                            ch_info = int(input('수정할 영어점수를 입력하세요. >> ')) 
                            stu['eng'] = ch_info
                            stu['total'] = stu['kor'] + stu['eng'] + stu['math']
                            stu['avg'] = stu['total'] / 3
                            print('국어점수가 수정되었습니다.')
                            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                                    stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg'],stu['rank']))    
                
                        elif change == 4:
                            ch_info = int(input('수정할 수학점수를 입력하세요. >> ')) 
                            stu['math'] = ch_info
                            stu['total'] = stu['kor'] + stu['eng'] + stu['math']
                            stu['avg'] = stu['total'] / 3
                            print('국어점수가 수정되었습니다.')
                            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                                    stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg'],stu['rank']))
                        
            if search == '0':
                break
        
        
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break           # # 여기
                    
                    
            
                
                
                    
                
                

            
        
            
        
        