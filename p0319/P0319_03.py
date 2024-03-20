class Student:
    count = 1       # 클래스 변수 사용
    
    def __init__(self,name,kor,eng,math,stuNo = 0,rank = 0):
        if stuNo == 0:
            self.stuNo = Student.count      # 클래스 변수 사용.
        else:
            self.stuNo = stuNo
                
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float('{:.2f}'.format(self.total/3))
        if rank != 0:
            self.rank = rank
            
    def __str__(self): # 객체를 호출하면 출력됨.
        return f'학생성적 : {self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}'
        
    
students = []

# 파일 불러오기
f = open('stu.txt','r',encoding='utf8')

while True:
    txt = f.readline()
    if txt == '' : break
    txt_list = txt.strip().split(',')
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4])
            ,int(txt_list[0]),int(txt_list[7]))    
    students.append(s)
    
    
    
print(students[2].kor)


f.close()

        
        