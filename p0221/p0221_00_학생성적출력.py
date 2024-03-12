
# stu_name = input("이름")
# kor = int(input("국어"))
# eng = int(input("영어"))
# math = int(input("수학"))
# total = int(kor+eng+math)
# avg = int(total/3)

# print(" 이름","\t", "국어점수","영어점수","수학점수","총점","평균")
# print(stu_name,'\t', kor,'\t',eng,'\t',math,'\t',int(total),'\t',int(avg))

stu_name = "홍길동"
kor = 100
eng = 100
math = 100
total = kor+eng+math
avg = total/3

print("이름","\t", "국어점수","\t","영어점수","\t","수학점수","\t","총점","\t","평균")
print(stu_name,'\t',"  %d"%kor,'\t','\t',"%d"%eng,'\t','\t',"%d"%math,'\t','\t',int(total),'\t',int(avg))


