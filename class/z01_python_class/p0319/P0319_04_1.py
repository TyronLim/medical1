#----------------------------------------------------------함수----------------------------------------#

#-----------------------------------------------메인화면 함수-----------------------------------------------------#
def stu_main_print():
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('7. 학생성적 파일저장')
    print('0. 프로그램종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요 >> ')
    if not choice.isdigit():
        print('숫자만 입력가능합니다.')
    choice = int(choice)
    return choice

#-----------------------------------------------성적출력화면 함수-----------------------------------------------------#
def stu_print():
    print('학생성적 전체출력')
    print('-'*50)
    print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
    print('-'*50)
    
#-----------------------------------------------학생입력 함수-----------------------------------------------------#
def stu_insert():
    cnt = len(students) + 1
    while True:
        ff = open('stu.txt','a',encoding='utf8')
        print('학생성적입력')
        name = input('입력할 학생의 이름을 입력하세요(0.취소) >> ')
        if name == '0': break
        
        kor = int(input('국어점수를 입력하세요 >> '))
        eng = int(input('영어점수를 입력하세요 >> '))
        math = int(input('수학점수를 입력하세요 >> '))
        total = kor + eng + math
        avg = total / 3
        rank = 0
        stuNo = cnt
        stu = Student(name,kor,eng,math,stuNo,rank)
        students.append(stu)
        cnt += 1
        print(stu)
        

        f.write(f'{stu.stuNo},{stu.name},{stu.kor},{stu.eng},{stu.math},{stu.total},{stu.avg},{stu.rank}\n')
        
    ff.close()


#-----------------------------------------------학생전체출력 함수-----------------------------------------------------#
def stu_all_print():
    stu_print()
    for i in students:
        print(i)    # 클래스 출력
    
    print()


#-----------------------------------------------학생검색(전체) 함수-----------------------------------------------------#
def stu_search_all():
    choice = stu_search_print()   
    if choice.isdigit():
        choice = int(choice)

    return choice

#-----------------------------------------------학생검색(일부) 함수-----------------------------------------------------#
def stu_search(choice):
    search = input(f'{search_txt[choice]}')
    s_list = []
    s_cnt = 0
    for i in students:
        if search in i.name:
            s_list.append(i)
        s_cnt +=1
    
    if len(s_list) == 0 :
        print('-'*50)
        print('검색 결과가 없습니다.')
        print('-'*50)

    else :
        print('-'*50)
        print('검색 결과')
        print('-'*50)
        for i in s_list:
            print(i)


#-----------------------------------------------학생검색 화면 함수-----------------------------------------------------#
def stu_search_print():
    print('[ 학생성적 검색 ]')
    print('1. 이름으로 검색')
    print('2. 점수이상 검색')
    print('3. 점수이하 검색')
    print('0. 이전 화면')
    choice = input('검색할 항목을 선택하세요 >> ')
    
    return choice
#------------------------------------g-------------------------------------------------------------#
def stu_update():
    print('[ 학생성적 수정 ]')
    search = input('수정할 학생의 이름을 입력해주세요 >> ')
    cnt = 0
    for i in students:
        if search == i.name:
            break
        cnt += 1
    
    if cnt == len(students):
        print('입력한 학생이 없습니다.')
    
    else : 
        print('-'*50)
        print(f'{search}학생의 정보입니다.')
        print(students[cnt])
        print('-'*50)
        s_choice = input('수정할 과목을 선택하세요 (1.국어 / 2.영어 / 3.수학 / 0.뒤로가기)')
        if s_choice.isdigit():
            s_choice = int(s_choice)
        
        if s_choice == 1:
            sub = ['','국어','영어','수학']
            # sub2 = ['',students[cnt].kor,students[cnt].eng,students[cnt].math]

            score = int(input(f'수정할 {sub[s_choice]}점수를 입력하세요'))
            
            with open('C:\workspace\medical1\python class\stu.txt','w',encoding='utf8') as ff:
                for i in range(len(students)):
                    if i == cnt-1:
                        # sub2[s_choice] = score      # 국어 점수 수정
                        up_stu = Student[score,students[i][3],students[i][4],students[i][0],0]
                        ff.write(up_stu.stuNo,up_stu.name,up_stu.kor,up_stu.eng,up_stu.math,up_stu.total,up_stu.avg,up_stu.rank)
                        
                    else:
                        up_stu = Student[score,students[i][3],students[i][4],students[i][0],0]
                        ff.write(up_stu.stuNo,up_stu.name,up_stu.kor,up_stu.eng,up_stu.math,up_stu.total,up_stu.avg,up_stu.rank)



#------------------------------------클래스 선언-------------------------------------------------------------#
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


#=========================================파일 불러오기=================================================================#
students = []

f = open('C:\workspace\medical1\python class\stu.txt','r',encoding='utf8')
    
while True:
    txt = f.readline()
    stu_list = txt.strip().split(',')
    # print(stu_list)
    if txt == '': break
    s = Student(stu_list[1],int(stu_list[2]),
                int(stu_list[3]),int(stu_list[4]),
                int(stu_list[0]),int(stu_list[7]))
    students.append(s)

for i in students:
    print(i)
    
    
while True:
    choice = stu_main_print()
    
    stu = []
    if choice == 1:         # 학생 입력
        stu_insert()

    elif choice == 2:       # 학생 전체 출력
        stu_all_print()

    elif choice == 3:       # 학생 검색
        search_txt = ['','찾을 학생의 이름을 입력하세요 >>','총점을 입력하세요 >>','총점을 입력하세요 >>']
        
        while True:                
            choice = stu_search_all()
                
            if choice == 1:
                stu_search(choice)

            elif choice == 2:
                search = int(input(f'{search_txt[choice]}'))
                s_list = []
                s_cnt = 0
                for i in students:
                    if search <= i.total:
                        s_list.append(i)
                    s_cnt +=1
                
                if len(s_list) == 0 :
                    print('-'*50)
                    print('검색 결과가 없습니다.')
                    print('-'*50)

                else :
                    print('-'*50)
                    print('검색 결과')
                    print('-'*50)
                    for i in s_list:
                        print(i)
                        
            elif choice == 3:
                search = int(input(f'{search_txt[choice]}'))
                s_list = []
                s_cnt = 0
                for i in students:
                    if search >= i.total:
                        s_list.append(i)
                    s_cnt +=1
                
                if len(s_list) == 0 :
                    print('-'*50)
                    print('검색 결과가 없습니다.')
                    print('-'*50)

                else :
                    print('-'*50)
                    print('검색 결과')
                    print('-'*50)
                    for i in s_list:
                        print(i)
            elif choice == 0:
                break
    
    elif choice == 4:       # 학생 성적 수정
        stu_update()
        
    f.close()