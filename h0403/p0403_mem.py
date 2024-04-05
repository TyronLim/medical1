class Stu:
    stuNo = 0
    cnt = 1

    def __init__(self,name,kor,eng,math,stuNo):
        if self.stuNo == 0:
            stuNo=Stu.cnt
            Stu.cnt+=1
        
        else:
            self.stuNo = stuNo
        
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)
        self.total = kor+eng+math
        self.avg = float("{:.2f}".format(total/3))
        self.rank = 0
        
    def __str__(self):
        return f"{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"


students=[]
cnt = len(students)+1
with open('student.txt','a',encoding='utf8') as f:

    while True:
        name=input('이름 >> ')
        if name == '0':
            break
        kor=int(input('국어 >> '))
        eng=int(input('영어 >> '))
        math=int(input('수학 >> '))
        total=kor+eng+math
        avg=float('{:.2f}'.format(total/3))
        student = Stu(name,kor,eng,math)
        
        # print(student)
        f.write("{},{}\n".format(cnt,student))
        cnt+=1


