students = [{'stuNo': 's001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
            {'stuNo': 's002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
            {'stuNo': 's003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
            {'stuNo': 's004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
            {'stuNo': 's005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

chk = 0
while True:
    del_stu = input('삭제할 학생의 이름을 입력해주세요. (0.취소)>> ')
    if del_stu == '0':
        print('취소하셨습니다.')
    
    for stu in students:
        if del_stu == stu['name']:
            break
        chk += 1
        
    if chk >= len(students):
        print('찾는 학생이 없습니다.')
    
    else : 
        print('학생을 찾았습니다.')
        print(students[chk])
        s_input = input('삭제하시겠습니까?(0.취소 / 1.삭제)')
        if s_input == 0:
            print('취소했습니다.')
            break        
        else :
            print('삭제되었습니다.')
            del students[chk]
    
    
    
    
    
    # for i, stu in enumerate(students):        
    #     if del_stu == stu['name']:
    #         print('{}학생에 대한 정보가 있습니다.'.format(del_stu))
    #         s_input = int(input('삭제하시겠습니까? (0.취소 / 1.삭제)>> '))
    #         if s_input == 0:
    #             break
    #         elif s_input == 1:
    #             del students[i]
    #             print('삭제되었습니다.')
                
    #     else:
    #         print('{}학생에 대한 정보가 없습니다.'.format(del_stu))
    
    print(students)
    
