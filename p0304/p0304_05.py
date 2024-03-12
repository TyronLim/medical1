# 학생 검색
students = [[1,'홍길동',100,100,100,300,100],
            [2,'유관순',90,90,90,270,90],
            [3,'이순신',80,80,80,240,80]]

chk = 0    # 찾는 정보 확인
while True:
    search = input('검색하고 싶은 학생 이름을 입력하세요.')   # 학생 입력
    if search == 0:
        break
    for stu in students:                                   # 학생 찾기
        if search in stu:
            chk = 1   # 정보를 찾았을 때 정보를 1로 변경
            break        
    
    if chk == 1:
        print('{}의 학생정보를 찾았습니다.'.format(search))
        print('[학생성적출력]')
        print('-'*50)
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
        print('-'*50)

    else :
        print('찾는 학생정보가 없습니다.')