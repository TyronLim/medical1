# 학생성적 입력
# 변수 사용

name = input('학생 이름을 입력하세요 >> ')
kor = int(input('국어 점수를 입력하세요 >>'))
eng = int(input('영어 점수를 입력하세요 >>'))
math = int(input('수학 점수를 입력하세요 >>'))
tot = kor+eng+math
avg = tot/3


# 입력을 받아서 총점과 평균을 계산하고 출력
# 홍길동 100 100 100 300 100.0

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format
      (1,name,kor,eng,math,tot,avg,1))

# stu1 = [1,name,kor,eng,math,tot,avg,1]
# stu2 = [2,name,kor,eng,math,tot,avg,2]
# stu3 = [3,name,kor,eng,math,tot,avg,3]

# stu



