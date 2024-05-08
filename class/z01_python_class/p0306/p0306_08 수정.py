# students = [S001, '홍길동', 100, 99, 87, 286, 95.33, 2],
#             [S002, '유관순', 98, 93, 87, 278, 92.67, 3],
#             [S003, '이순신', 88, 76, 30, 194, 64.67, 5],
#             [S004, '김구', 100, 100, 100, 300, 100.00, 1],
#             [S005, '강감찬', 98, 85, 44, 227, 75.67, 4]]

students = [{'stuNo': 's001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
            {'stuNo': 's002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
            {'stuNo': 's003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
            {'stuNo': 's004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
            {'stuNo': 's005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

subject = ['순번','학번','이름','국어','영어','수학','합계','평균','등수']
cnt = len(students)+1 # 학번

s_title = ['','국어','영어','수학']
while True:
    name = input('찾는 학생의 이름을 입력하세요(0.취소) >> ')
    chk = 0
    if name == '0':
        print('학생수정을 취소합니다.')
        break
    
    for i in students:
        if name == i['name']:
            break
        chk += 1    
            
    if chk == len(students):        # 없으면 (for문을 다 돌고나서 +1이 더 되었을 때) 
        print('없습니다.')
    
    else : 
        print('학생 정보를 찾았습니다.')

        while True:
            print('(1.국어\t2.영어\t3.수학\t0.취소)')
            subject_input = int(input('수정하려는 과목을 선택하세요.'))
            
            if subject_input == 1:
                s_1 = 'kor'
                # 함수            
                # s_update(s_1)
                print('[{}수정]'.format(s_title[subject_input]))
                print('현재 {}점수 :{}'.format(s_title[subject_input], students[chk][s_1]))
                print('-'*40)                
                score = int(input('수정할 {}점수를 입력하세요 >> '.format(s_title[subject_input])))
                students[chk][s_1] = score
                students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']
                students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3))
                print('{}점수 : {}점으로 수정이 완료되었습니다.'.format(s_title[subject_input], students[chk][s_1]))
                print(students[chk])
                print('-'*40)  

            elif subject_input == 2:
                s_1 = 'eng'
                # 함수
                # s_update(s_1)
                print('현재 {}점수 :{}'.format(s_title[subject_input], students[chk][s_1]))
                print('-'*40)                
                score = int(input('수정할 {}점수를 입력하세요 >> '.format(s_title[subject_input])))
                students[chk][s_1] = score
                students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']
                students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3))
                print('{}점수 : {}점으로 수정이 완료되었습니다.'.format(s_title[subject_input], students[chk][s_1]))
                print(students[chk])
                print('-'*40)  
                
            elif subject_input == 3:
                s_1 = 'math'
                # 함수
                # s_update(s_1)
                print('현재 {}점수 :{}'.format(s_title[subject_input], students[chk][s_1]))
                print('-'*40)                
                score = int(input('수정할 {}점수를 입력하세요 >> '.format(s_title[subject_input])))
                students[chk][s_1] = score
                students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']
                students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3))
                print('{}점수 : {}점으로 수정이 완료되었습니다.'.format(s_title[subject_input], students[chk][s_1]))
                print(students[chk])
                print('-'*40)  
                
                
            elif subject_input == 0:
                print('과목 수정을 취소합니다.')
                break
            
            else :
                print('올바른 번호를 입력해주세요.')


# 함수선언
# def s_update(s_1):
#     print('[{}수정]'.format(s_title[subject_input]))
#     print('현재 {}점수 :{}'.format(s_title[subject_input], students[chk][s_1]))
#     print('-'*40)                
#     score = int(input('수정할 {}점수를 입력하세요 >> '.format(s_title[subject_input])))
#     students[chk][s_1] = score
#     students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']
#     students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3))
#     print('{}점수 : {}점으로 수정이 완료되었습니다.'.format(s_title[subject_input], students[chk][s_1]))
#     print(students[chk])
#     print('-'*40)  


