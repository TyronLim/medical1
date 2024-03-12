# 2명의 학생의 국어, 영어, 수학을 입력받아
# 합계를 출력하세요

students = []
for i in range(0,2):
    student = []  
    student.append(input('이름 입력 >> '))
    student.append(int(input('국어 성적 >> ')))
    student.append(int(input('영어 성적 >> ')))
    student.append(int(input('수학 성적 >> ')))
    sum = student[1]+student[2]+student[3]
    avg = sum/3
    student.append(sum)
    student.append('{:.2f}'.format(avg))
    students.append(student)
# print(students)
# for i in range(0,2):
#     kor = int(input('국어 성적 >> '))
#     eng = int(input('영어 성적 >> '))
#     math = int(input('수학 성적 >> '))
#     student.append(kor,eng,math)
#     students.append(student)


# 합계
# print(students)

# 전체학생출력
print('[학생성적출력]')
print('-'*50)
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*50)
 # 2차원 리스트 for문 2번 사용
for stu in students:    
    for i in stu:
        print(i,end='\t')
    print()
print()
print('-'*30)

 # 3명의 국어점수 합계, 평균 출력하기
 
korsum = 0
engsum = 0
mathsum = 0
totals = 0
koravg = 0

for i,stu in enumerate(students):    
    korsum = korsum + stu[1]
    engsum = engsum + stu[2]
    mathsum = mathsum + stu[3]
    totals += stu[4]
    # koravg = korsum / i+1
    
avg
print(korsum)
print(engsum)
print(mathsum)
print(totals)
print(koravg)
    
    
print('세 학생의 국어 총합은 =',korsum)
print('세 학생의 국어 평균은 =',koravg)   # korsum / 3
print('-'*30)


