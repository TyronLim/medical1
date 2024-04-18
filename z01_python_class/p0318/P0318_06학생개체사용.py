class Student:              # 클래스 선언
    # stuNo = 0
    # name = ''
    # kor = 0
    # eng = 0
    # math = 0
    # total = 0
    # avg = 0
    # rank = 0                              init에 self로 넣으면 굳이 기본값 안 넣어도 됨.
    
    # def cal_total(self,kor,eng,math):
    #     self.total = kor+eng+math
        
    # def cal_avg(self,total):
    #     self.avg = float(total/3)
    
    
    def __init__(self,stuNo,name,kor,eng,math):
        self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float('{:.2f}'.format(self.total / 3))
        self.rank = 0
        

# total = s1.cal_total(99,99,87)
# avg = s1.cal_avg(total)

s1 = Student(1,'홍길동',99,99,87)
print('{} {} {} {} {} {} {:.2f} {}'.format(s1.stuNo,s1.name,s1.kor,s1.eng,s1.math,s1.total,s1.avg,s1.rank))

s2 = Student(2,'유관순',98,83,87)
print('{} {} {} {} {} {} {:.2f} {}'.format(s2.stuNo,s2.name,s2.kor,s2.eng,s2.math,s2.total,s2.avg,s2.rank))
        
s3 = Student(3,'이순신',88,76,30)
print('{} {} {} {} {} {} {:.2f} {}'.format(s3.stuNo,s3.name,s3.kor,s3.eng,s3.math,s3.total,s3.avg,s3.rank))


stu_list = [s1,s2,s3]
for i in stu_list:
    print(i.stuNo, i.name)







# s1 = Student()
# s1.stuNo = 1
# s1.name = '홍길동'
# s1.kor = 99
# s1.eng = 99
# s1.math = 87
# s1.total = s1.kor+s1.eng+s1.math
# s1.avg = s1.total / 3
# s1.rank = 1
# print(s1.stuNo,s1.name,s1.kor,s1.eng,s1.math,s1.total,s1.avg,s1.rank)

# s2 = Student()
# s2.stuNo = 2
# s2.name = '유관순'
# s2.kor = 98
# s2.eng = 93
# s2.math = 87
# s2.total = s2.kor+s2.eng+s2.math
# s2.avg = s2.total / 3
# s2.rank = 3
# print(s2.stuNo,s2.name,s2.kor,s2.eng,s2.math,s2.total,s2.avg,s2.rank)

# s3 = Student()
# s3.stuNo = 3
# s3.name = '이순신'
# s3.kor = 88
# s3.eng = 76
# s3.math = 30
# s3.total = s3.kor+s3.eng+s3.math
# s3.avg = s3.total / 3
# s3.rank = 1
# print(s1.stuNo,s1.name,s1.kor,s1.eng,s1.math,s1.total,s1.avg,s1.rank)