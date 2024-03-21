class Student:
    
    def __init__(self,name,kor,eng,math):
        self.__name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math

    def stu_print(self):
        print('학생성적 출력합니다.')

    def __str__(self):
        return f'{self.__name},{self.kor},{self.eng},{self.math},{self.total}'
    
    def set_name(self,name):
        self.__name = name

# def s_print():
#     print('class 밖에서 출력합니다.')


    
s = Student('유관순',100,100,100)

s.name = '홍길동'
s.set_name = '홍길동'


# s.stu_print()

print(s)

# if isinstance(s,Student):
#     print('ok')

# else :
#     print('no')
    
    
# print(s)