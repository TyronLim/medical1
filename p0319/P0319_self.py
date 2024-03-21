class Student:
    stuNo = 0
    rank = 0
    cnt = 1
    
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if self.stuNo == 0:
            self.stuNo = Student.cnt
            Student.cnt += 1
        
        else :
            self.stuNo = stuNo
            
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float('{:.2f}'.format(self.total / 3))

        if self.rank != 0:
            self.rank = rank
    
    def __str__(self):
        return f'{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}'


students = []

with open('stu.txt','r',encoding='utf8') as f:
    cnt = 0
    while True:
        txt = f.readline()
        stu_list = txt.strip().split(',')
        # print(stu_list)
        if txt == '': break
        with open('stu.txt','w',encoding='utf8') as ff:
            s = Student(stu_list[1],int(stu_list[2]),int(stu_list[3]),int(stu_list[4]),int(stu_list[0]),int(stu_list[7]))
            ff.write(f'{stu_list[0]},{stu_list[1]},{stu_list[2]},{stu_list[3]},{stu_list[4]},{stu_list[5]},{stu_list[6]},{stu_list[7]}\n')
            if cnt == 1:
                s1 = Student(f'{stu_list[0]},{stu_list[1]},{80},{stu_list[3]},{stu_list[4]},{stu_list[5]},{stu_list[6]},{stu_list[7]}\n')          
                ff.write(s1)
        students.append(s)#write 써
        
        cnt += 1
        
for i in students:
    print(i)

# a = []

# for i in students:
#     a.append(i)

# for i in a:
#     print(i)


# with open('stu.txt','w',encoding=('utf8')) as ff:
#     for i in students:
#         f.write(f'{i}\n')

# a = [[1,2,3,4,5],[6,7,8,9,10]]

# with open('a.txt','w',encoding='utf8') as f:
#     for i in a:      
#         f.write(f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n')