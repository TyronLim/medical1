student = [[1,'홍길동',100,100,100,300,100.0,1], 
           [2,'유관순',90,90,90,270,90.0,2]]

print('-'*35)
print('\t[학생성적프로그램]')
print('1.학생성적입력')
print('4.학생성적전체출력')
print('-'*35)
ch = int(input('원하는 번호를 입력하세요 > '))

if ch == 1:
    print('학생성적입력을 선택하셨습니다.')
    name3 = input('학생의 이름을 입력해주세요 >')
    kor3 = int(input('학생의 국어성적을 입력해주세요 >'))
    eng3 = int(input('학생의 영어점수를 입력해주세요 >'))
    math3 = int(input('학생의 수학점수를 입력해주세요 >'))
    stu3 = [0,'',0,0,0,0,0.0,3]
    stu3[0]=3
    stu3[1]=name3
    stu3[2]=kor3
    stu3[3]=eng3
    stu3[4]=math3
    stu3[5]=kor3+eng3+math3
    stu3[6]=(kor3+eng3+math3)/3
    
    # stu3 = []                          > line(stu3)에 값 입력하는 다른 방법
    # stu3.append(3)
    # stu3.append(name3)
    # stu3.append(kor3)
    # stu3.append(eng3)
    # stu3.append(math3)
    # stu3.append(kor3+eng3+math3)
    # stu3.append(kor3+eng3+math3)/3)
    
    # stu3 = [3,name3,kor3,eng3,math3,kor3+eng3+math3,(kor3+eng3+math3)/3]   # 또 다른 방법
    
    print('입력하신 정보는 {}입니다'.format(stu3))
    student.append(stu3)
    print('-'*35)
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        student[0][0],student[0][1],student[0][2],student[0][3],student[0][4],student[0][5],
        student[0][6],student[0][7]))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        student[1][0],student[1][1],student[1][2],student[1][3],student[1][4],student[1][5],
        student[1][6],student[1][7]))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        student[2][0],student[2][1],student[2][2],student[2][3],student[2][4],student[2][5],
        student[2][6],student[2][7]))
    print('-'*35)
    
elif ch == 4:
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        student[0][0],student[0][1],student[0][2],student[0][3],student[0][4],
        student[0][5],student[0][6],student[0][7]))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        student[1][0],student[1][1],student[1][2],student[1][3],student[1][4],
        student[1][5],student[1][6],student[1][7]))
else :
    print('올바른 번호를 입력하세요.')
    
print(student)



