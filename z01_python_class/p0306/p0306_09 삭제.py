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


cnt = len(students)+1 # 학번

while True:
    search = input('삭제하고자 하는 학생의 이름을 입력하세요(0.취소) >> ')
    chk = 0
    if search == '0':
        print('학생수정을 취소합니다.')
        break
    
    for i in students:
        if search == i['name']:
            break
        chk += 1    
            
    print('찾고자 하는 학생의 위치 :',chk)
    
    if chk >= len(students):
        print('찾고자 하는 학생이 없습니다.')
    else :
        print(f'{search}학생의 정보가 있습니다')
        s_input = input(f'{search}학생 성적을 삭제하시겠습니까?(0. 취소, 1. 삭제)')
        #삭제
        if s_input != '1':
            print('f{search}학생의 삭제를 취소했습니다.')
            break
        else : 
            del students[chk]
            print(f'{search}학생의 성적이 삭제되었습니다.')
            
    print(students)
    
        
            