print('\t[학생성적프로그램]')
print('-'*35)
print('1.학생성적입력')
print('2.학생성적수정')
print('3.학생성적삭제')
print('4.학생성적전체출력')
print('5.학생검색출력')
print('6.등수처리')
print('0.프로그램종료')
print('-'*35)



stu1_name=input('학생1의 이름을 입력하세요 : ')
stu1_kor=int(input('학생1의 국어점수를 입력하세요 : '))
stu1_eng=int(input('학생1의 영어점수를 입력하세요 : '))
stu1_math=int(input('학생1의 수학점수를 입력하세요 : '))
tot1=stu1_kor+stu1_eng+stu1_math
avg1=tot1/3

stu2_name=input('학생2의 이름을 입력하세요 : ')
stu2_kor=int(input('학생2의 국어점수를 입력하세요 : '))
stu2_eng=int(input('학생2의 영어점수를 입력하세요 : '))
stu2_math=int(input('학생2의 수학점수를 입력하세요 : '))
tot2=stu2_kor+stu2_eng+stu2_math
avg2=tot2/3

# print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
# print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.\
#     format(1,stu1_name,stu1_kor,stu1_eng,stu1_math,\
#         tot1,avg1,1))
# print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.\
#     format(2,stu2_name,stu2_kor,stu2_eng,stu2_math,\
#         tot2,avg2,1))

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print("%d\t%s\t%d\t%d\t%d\t%d\t%.2f\t%d"%(1,stu1_name,stu1_kor,stu1_eng,stu1_math,\
    tot1,avg1,1))
print("%d\t%s\t%d\t%d\t%d\t%d\t%.2f\t%d"%(2,stu2_name,stu2_kor,stu2_eng,stu2_math,\
    tot2,avg2,2))

