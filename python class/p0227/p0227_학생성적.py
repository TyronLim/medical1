student= []

for i in range(5) : 
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1. 학생성적입력')
    print('4. 학생성적전체출력')
    print('0. 프로그램 종료')
    print('-'*35)
    ch = int(input('원하는 번호를 입력하세요 >>  '))
    if ch == 1:
        print('학생성적입력을 선택하셨습니다.')
        name = input('학생의 이름을 입력하세요 >')
        kor = int(input('학생의 국어점수를 입력하세요 >'))
        eng = int(input('학생의 영어점수를 입력하세요 >'))
        math = int(input('학생의 수학점수를 입력하세요 >'))
        tot = kor+eng+math
        avg = tot/3
        stu = [name,kor,eng,math,tot,avg]
        student.append(stu)
        print('입력하신 정보는 \n{}\n입니다.'.format(stu))
    elif ch == 4:
        print('학생전체출력을 선택하셨습니다.')
        print('-'*35)
        print('번호\t이름\t국어\t수학\t영어\t총점\t평균\t등수')
        for j in range(len(student)):
            rank = j+1
            num = j+1
            print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
            num, student[j][0],student[j][1],student[j][2],student[j][3],
            student[j][4],student[j][5],rank
            ))
        print('-'*35)
    elif ch == 0:
        print('프로그램 종료를 선택하셨습니다.')

print('프로그램을 종료합니다.')