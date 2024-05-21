students = [[1, '홍길동', 40, 100, 100, 240, 80.00, 0],
            [2, '유관순', 100, 85, 100, 285, 95.00, 0],
            [3, '이순신', 96, 96, 96, 288, 96.00, 0],
            [4, '김구', 90, 80, 73, 243, 81.00, 0],
            [5, '김유신', 70, 60, 90, 220, 73.33, 0],
            [6, '강감찬', 100, 100, 100, 300, 100.00, 0]]

# 등수처리
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