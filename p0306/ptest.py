students = [{'stuNo': 's001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
            {'stuNo': 's002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
            {'stuNo': 's003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
            {'stuNo': 's004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
            {'stuNo': 's005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}]

choice = input('번호 입력')
if choice == '4':
    print('번호입력을 선택하셨습니다.')

while True:
    cnt = 0 
    name = input('수정할 이름을 취소는0>>')
    if name == '0':
        print('취소')
        break
    for i in students:
        if name == i['name']:
            break
        cnt += 1
    print(f'학생 위치 : {cnt}')