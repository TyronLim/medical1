class Student:
    name = ''
    kor = 0
    
    # def __init__(self):
    #     pass

    def stu_print(self):
        print('학생성적 출력합니다.')

def s_print():
    print('class 밖에서 출력합니다.')


    
s = Student()

s.stu_print()

print(s)

if isinstance(s,Student):
    print('ok')

else :
    print('no')