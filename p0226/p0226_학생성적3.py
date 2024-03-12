student = []

for i in range(5) : 
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1. 학생성적입력')
    print('4. 학생성적전체출력')
    print('0. 프로그램 종료')
    print('-'*35)
    ch = input('원하는 번호를 입력하세요 >>  ')
    if ch == '1':
        print(['학생성적입력'])
        name = input('학생 이름 >')
        kor = int(input('국어 >'))
        eng = int(input('영어 >'))
        math = int(input('수학 >'))
        stu = [name,kor,eng,math]
        print(stu)
        student.append(stu)
    
    elif ch == '4':
        print('[학생성적전체출력]')
        print('이름\t국어\t영어\t수학')
        for j in range(len(student)):
            print(print('{}\t{}\t{}\t{}'.format(
                student[j][0],student[j][1],student[j][2],student[j][3])))
        
    
        
    