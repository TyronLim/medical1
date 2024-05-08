class Student:
    stuCount = 0
    stuNo = 0
    
    def __init__(self,name,kor,eng,math):    # 생성자 __init__ : 클래스에 대해 객체선언을 하면 제일 먼저 호출되는 함수.
        self.name = name
        self.kor = kor
        if 0<=kor<=100:
            self.kor = 100

        else :
            self.kor = kor
            
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float('{:.2f}'.format(self.total/3))
        self.rank = 0
        Student.stuCount += 1  # 클래스변수 선언
        self.stuN0 = Student.stuCount
        
    def s_print(self):
        print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        (f'{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}')

    def __str__(self):
        return (f'{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}')
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        self.stuNo,self.name,self.kor,self.eng,self.math,self.total,self.avg,self.rank))
        
# 매개변수가 있는 객체(인스턴스) 선언
s1 = Student('홍길동',200,100,99)
s2 = Student('유관순',99,99,98)

s1.s_print('유관순',99,99,98)
s2.s_print()
