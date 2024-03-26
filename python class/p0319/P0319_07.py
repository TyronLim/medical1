#----------------------------------------함수 메인화면---------------------------------------------------------------#
def stu_print():
    print("-"*40)
    print("[ 학생성적프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적전체입력")
    print("3. 학생검색")
    print("4. 학생성적수정")
    print('5. 학생삭제')
    print('6. 등수처리')
    print('7. 학생성적 파일저장')
    print('0. 프로그램종료')
    print("-"*40)
    choice = input("원하는 번호를 입력하세요.>> ")
    
    if choice.isdigit():
        choice = int(choice)
    
    return choice

#----------------------------------------함수 학생입력---------------------------------------------------------------#
def stu_insert():
    stu_count = len(students)+1
    while True:
        print('[ 학생성적입력 ]')
        print('-'*60)
        name = input('입력할 학생의 이름을 선택해주세요. (0.뒤로가기) >> ')
        if name == '0': break
        kor = int(input('국어점수를 입력하세요 >> '))
        eng = int(input('영어점수를 입력하세요 >> '))
        math = int(input('수학점수를 입력하세요 >> '))
        s1 = Student(name,kor,eng,math,stu_count,0)
        students.append(s1)
        stu_count += 1
        print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
        print('-'*60)
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
            students[-1].stuNo,students[-1].name,students[-1].kor,students[-1].eng,students[-1].math,
            students[-1].total,students[-1].avg,students[-1].rank))

#----------------------------------------함수 학생성적전체출력--------------------------------------------------------#
def stu_all_print():
    print('[ 학생성적전체출력 ]')
    print('-'*60)
    print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
    print('-'*60)
    for i in students:
        print(i)
    print('-'*60)

#----------------------------------------함수 학생검색---------------------------------------------------------------#
def stu_search():
    while True:
        cnt = 0
        print('[ 학생검색 ]')
        print('-'*60)
        search = input('검색할 학생의 이름을 입력해주세요(0.뒤로가기) >> ')
        if search == '0': break
        for i in students:
            if search == i.name:
                print(f'{search}학생에 대한 정보가 있습니다.')
                print('-'*60)
                print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                print('-'*60)
                print(i)
            else :
                cnt += 1
        
        if cnt == len(students):
            print(f'{search}학생에 대한 정보가 없습니다. 다시 입력해주세요')

#----------------------------------------함수 성적수정---------------------------------------------------------------#
def stu_update():
    while True:
        cnt = 0
        print('[ 학생성적수정 ]')
        print('-'*60)
        search = input('검색할 학생의 이름을 입력해주세요(0.뒤로가기) >> ')
        if search == '0': break
        
        sub = ['','국어','영어','수학']
        sub2 = ['',students[cnt].kor,students[cnt].eng,students[cnt].math]
        for i in students:
            if search == i.name:
                print(f'{search}학생에 대한 정보가 있습니다.')
                print('-'*60)
                print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                print('-'*60)
                print(i)
                
                choice = input('수정할 과목을 선택해주세요 (1.국어 / 2.영어 / 3.수학 )>> ')
                if choice.isdigit():
                    choice = int(choice)
            
                if choice == 1:
                    sub_up = input(f'수정할 {sub[choice]}국어 점수를 입력해주세요 >> ')
                    if sub_up.isdigit():
                        sub_up = int(sub_up)
                    students[cnt].kor = sub_up     
                    students[cnt].total = students[cnt].kor + students[cnt].eng + students[cnt].math
                    students[cnt].avg = float('{:.2f}'.format(students[cnt].total/3))
                    print('{sub[choice]} 점수가 수정되었습니다.')
                    print('-'*60)
                    print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                    print('-'*60)
                    print(students[cnt]) 
                    
                elif choice == 2:
                    sub_up = input(f'수정할 {sub[choice]} 점수를 입력해주세요 >> ')
                    if sub_up.isdigit():
                        sub_up = int(sub_up)
                    students[cnt].eng = sub_up     
                    students[cnt].total = students[cnt].kor + students[cnt].eng + students[cnt].math
                    students[cnt].avg = float('{:.2f}'.format(students[cnt].total/3))
                    print(f'{sub[choice]} 점수가 수정되었습니다.')
                    print('-'*60)
                    print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                    print('-'*60)
                    print(students[cnt]) 
                    
                elif choice == 3:
                    sub_up = input(f'수정할 {sub[choice]} 점수를 입력해주세요 >> ')
                    if sub_up.isdigit():
                        sub_up = int(sub_up)
                    students[cnt].math = sub_up     
                    students[cnt].total = students[cnt].kor + students[cnt].eng + students[cnt].math
                    students[cnt].avg = float('{:.2f}'.format(students[cnt].total/3))
                    print(f'{sub[choice]} 점수가 수정되었습니다.')
                    print('-'*60)
                    print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                    print('-'*60)
                    print(students[cnt])     
        
            else :
                cnt += 1
        
        if cnt == len(students):
            print(f'{search}학생에 대한 정보가 없습니다. 다시 입력해주세요.')
            
#----------------------------------------함수 학생삭제---------------------------------------------------------------#
def stu_delete():
    while True:
        print('[ 학생삭제 ]')
        cnt = 0
        search = input('삭제할 학생의 이름을 입력하세요(0.뒤로가기)')     
        if search == '0':break
        for i in students:
            if search == i.name:
                print(f'{search}학생의 정보가 있습니다.')
                choice2 = input('삭제하시겠습니까? (1.삭제 / 0.취소) >> ')
                if choice2.isdigit():
                    choice2 = int(choice2)
                if choice2 == 0:
                    print('학생삭제를 취소합니다.')
                    break
                elif choice2 == 1:
                    del students[cnt]
                    print(f'{search}학생의 정보를 삭제했습니다.')
                    print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                    print('-'*60)
                    for i in students:
                        print(i)
                    
            else :
                cnt += 1
        
        if cnt == len(students):
            print('입력한 학생의 정보가 없습니다. 다시 입력해주세요.')   

#----------------------------------------함수 등수처리---------------------------------------------------------------#
def stu_rank():
    print('[ 학생등수처리 ]')
    choice = input('등수처리를 하시겠습니까?(0.취소 / 1.처리)')
    if choice.isdigit():
        choice = int(choice)
    
    if choice == 0:
        print('등수처리가 취소되었습니다.')
    
    elif choice == 1:
        r_cnt = 1
        for i in students:
            i.rank = 1
            for j in students:
                if i.total < j.total:
                        i.rank += r_cnt
        r_cnt += 1
                
        print('등수처리가 완료되었습니다.')
        print('-'*60)
        print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
        for i in students:
            print(i)

#----------------------------------------함수 파일저장---------------------------------------------------------------#
def stu_save():
    print('학생성적파일저장')
    choice = input('파일을 저장하시겠습니까? (0.취소 / 1.저장)>')
    if choice.isdigit():
        choice = int(choice)
    if choice == 0:
        print('저장을 취소합니다.')
        
    elif choice == 1:
        with open('C:\workspace\medical1\student1.txt','w',encoding='utf8') as ff:
            for i in students:
                stu = Student(i.name,i.kor,i.eng,i.math,i.stuNo,i.rank)
                student = f'{stu.stuNo},{stu.name},{stu.kor},{stu.eng},{stu.math},{stu.total},{stu.avg},{stu.rank}'
                ff.write(f'{student}\n')
    
    else : 
        print('올바른 번호를 입력해주세요.')
        
        print('저장이 완료되었습니다.')

#----------------------------------------클래스 선언---------------------------------------------------------------#
class Student:
    s_cnt = 1
    rank = 0
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo == 0:
            self.stuNo = Student(s_cnt)
            s_cnt += 1
        else :
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float('{:.2f}'.format(self.total/3))
        self.rank = rank

    def __str__(self):
        return f'{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}'


#----------------------------------------파일 open---------------------------------------------------------------#
students = []
f = open("student1.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "": break
    txt_list = txt.split(",")
    # 1,홍길동,99,99,87,285,95.0,1
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
f.close()
#----------------------------------------끝---------------------------------------------------------------------#

#----------------------------------------여기서부터 본문--------------------------------------------------------------#

while True:
    choice = stu_print()
    
    if choice == 1:
        stu_insert()
    
    elif choice == 2:
        stu_all_print()
    
    elif choice == 3:
        stu_search()
  
    elif choice == 4:
        stu_update()
        
    elif choice == 5:
        stu_delete()                        
        
    elif choice == 6:
        stu_rank()

    elif choice == 7:    
        stu_save()
        
    elif choice == 0:
        print('학생성적프로그램을 전체 종료합니다.')
        break

    