student = []

# 두 명 이상의 학생의 (이름, 국, 영, 수) 를 입력받아/ 리스트 생성 후/ student 리스트에 넣어주세요
# student 리스트 전체 출력

name1 = input('학생1의 이름 > ')
kor1 = int(input('학생1의 국어점수 > '))
eng1 = int(input('학생1의 영어점수 > '))
math1 = int(input('학생1의 수학점수 > '))
tot1 = kor1+eng1+math1
avg1 = tot1 / 3

name2 = input('학생2의 이름 > ')
kor2 = int(input('학생2의 국어점수 > '))
eng2 = int(input('학생2의 영어점수 > '))
math2 = int(input('학생2의 수학점수 > '))
tot2 = kor2+eng2+math2
avg2 = tot2 / 3

stu1 = [name1, kor1, eng1, math1, '{}, {:.2f}'.format(kor1+eng1+math1,(kor1+eng1+math1)/3)]
stu2 = ['{}, {}, {}, {}, {}, {:.2f}'.format(name2, kor2, eng2, math2, tot2, avg2)]


# stu1 = ['',0,0,0]   > 넣을 위치에 기본값과 길이가 설정 되어 있어야 함.
# stu1[0] = 이름
# stu1[1] = 국어
# stu1[2] = 영어
# stu1[3] = 수학


student.append(stu1)
student.append(stu2)

print(student)