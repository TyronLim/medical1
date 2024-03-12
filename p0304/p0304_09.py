students = [[1, '홍길동', 40, 100, 100, 240, 80.00, 0],
            [2, '유관순', 100, 85, 100, 285, 95.00, 0],
            [3, '이순신', 96, 96, 96, 288, 96.00, 0],
            [4, '김구', 90, 80, 73, 243, 81.00, 0],
            [5, '김유신', 70, 60, 90, 220, 73.33, 0],
            [6, '강감찬', 100, 100, 100, 300, 100.00, 0]]

while True:
    search = input('삭제하려는 학생을 입력하세요.')
    cnt = 0 # 찾은 학생의 위치
    for i,stu in enumerate(students):                 # 이름 찾기(for문)
        if stu[1] == search:
            break
        cnt += 1

    if cnt == len(students):
        print('{}학생에 대한 정보가 없습니다.'.format(search))

    else :
        print('{}학생에 대한 정보가 있습니다.'.format(search))
        del students[cnt]
    print(students)
    print(cnt) 