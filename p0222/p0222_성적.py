name1 = input('학생1의 이름을 입력하세요 : ')
kor1 = int(input('학생1의 국어점수를 입력하세요 : '))
eng1 = int(input('학생1의 영어점수를 입력하세요 : '))
math1 = int(input('학생1의 수학점수를 입력하세요 : '))
tot1 = kor1+eng1+math1
avg1 = tot1/3

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(1,name1,kor1,eng1,math1,tot1,avg1,1))

if avg1>=80 : 
    print('{}님 합격입니다.'.format(name1))
else :
    print('{}님 불합격입니다.'.format(name1))




