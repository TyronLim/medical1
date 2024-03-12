students= {'stuNo':1, 'stuName':'홍길동', 'tel':'010-0000-0000',
           'gender':'male', 'id':'aaa', 'pw':1111}

if 'studentNo' in students:
    print('key가 있습니다')
    students['studentNo'] += 1  # 키 값이 없는 걸 가져오면 에러가 남
    print(students['studentNo'])

else :
    print('key가 없습니다.')
    
    
