# 파일추가
import stu_file

s_title = ['','국어','영어','수학']

# stu.txt 파일열기호출
students = stu_file.stu_open()
#--------------------------------------------------------------------------------------#
def stu_first_screen():         # 첫 화면 함수
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요 >> ')
    if not choice.isdigit():
        print('숫자만 입력가능합니다.')
    choice = int(choice)
    
    return choice
#--------------------------------------------------------------------------------------#
def stu_input(cnt):
    while True:
        name = input(f'{len(students)+1}번째 학생의 이름을 입력하세요 (0. 취소)>> ')
        if name == '0':
            print('학생 입력을 취소합니다.')
            break
        student = {}   # 데이터 초기화
        student['stuNo'] = cnt
        student['name'] = name    # 딕셔너리 추가
        kor = int(input('국어점수를 입력하세요. >> '))
        student['kor'] = kor
        eng = int(input('영어점수를 입력하세요. >> '))
        student['eng'] = eng
        math = int(input('수학점수를 입력하세요. >> '))
        student['math'] = math
        total = kor + eng + math
        student['total'] = total
        avg = total / 3
        student['avg'] = float("{:.2f}".format(avg))
        students.append(student)    # list에 추가
        cnt += 1
        
        print('입력 데이터 :', student)
        print(students)
#--------------------------------------------------------------------------------------#
def stu_print_list():
    print('[학생전체출력]')
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('-'*65)
#--------------------------------------------------------------------------------------#
def stu_print_all(stu_list):
    while True : 
        count = input(('학생전체출력을 선택하시겠습니까?(1.확인, 2.취소) >> '))
        if count == '2':
            break
        stu_print_list()
        for s_dic in stu_list:
            for s_key in s_dic:
                print(s_dic[s_key],end='\t')
            print()
        print('-'*65)
        print()
 

#--------------------------------------------------------------------------------------#
def stu_print_search():
    search_students = []
    print('[ 학생성적검색 ]')
    search = input('찾고자하는 학생의 이름을 입력하세요>> ')
    
    # 검색한 이름으로 리스트에서 해당 학생 검색
    search_cnt = 0
    for s in students:
        if search == s['name']:
            break
        search_cnt +=1
        
    if search_cnt == len(students):
        print('찾고자 하는 학생이 없습니다. 다시 검색하세요.')
        
    else :
        print('{}학생을 찾았습니다. 성적을 출력합니다.'.format(search))
        # 1명의 학생을 리스트에 추가        
        search_students.append(students[search_cnt])
        stu_print_all(students)         # 학생성적전체출력함수 호출 


#--------------------------------------------------------------------------------------#
def stu_update_subject(subject_input,chk,s_1):
    print('[{}수정]'.format(s_title[subject_input]))
    print('현재 {}점수 :{}'.format(s_title[subject_input],students[chk][s_1]))
    print('-'*40)                
    score = int(input('수정할 {}점수를 입력하세요 >> '.format(s_title[subject_input])))
    students[chk][s_1] = score
    students[chk]['total'] = students[chk]['kor']+students[chk]['eng']+students[chk]['math']
    students[chk]['avg'] = float('{:.2f}'.format(students[chk]['total']/3))
    print('{}점수 : {}점으로 수정이 완료되었습니다.'.format(s_title[subject_input], students[chk][s_1]))
    print(students[chk])
    print('-'*40) 
#--------------------------------------------------------------------------------------#
def stu_rank():
    for s_dic in students:
        rank_cnt = 1 # 등수 처리변수
        for j_dic in students:
            if s_dic['total'] < j_dic['total']:
                rank_cnt += 1
        
        s_dic['rank'] = rank_cnt
    
    print('등수처리가 완료되었습니다.')    
    print(students)

def stu_update_list():
    s_title = ['','국어','영어','수학']
    while True:
        name = input('찾는 학생의 이름을 입력하세요(0.취소) >> ')
        chk = 0
        if name == '0':
            print('학생수정을 취소합니다.')
            break
        
        for i in students:
            if name == i['name']:
                break
            chk += 1    
                
        if chk == len(students):        # 없으면 (for문을 다 돌고나서 +1이 더 되었을 때) 
            print('없습니다.')
        
        else : 
            print('학생 정보를 찾았습니다.')

            while True:
                print('(1.국어\t2.영어\t3.수학\t0.취소)')
                subject_input = int(input('수정하려는 과목을 선택하세요.'))
                
                if subject_input == 1:
                    s_1 = 'kor'
                    stu_update_subject(subject_input,chk,s_1)

                elif subject_input == 2:
                    s_1 = 'eng'
                    stu_update_subject(subject_input,chk,s_1)
                    
                elif subject_input == 3:
                    s_1 = 'math'
                    stu_update_subject(subject_input,chk,s_1) 
                    
                    
                elif subject_input == 0:
                    print('과목 수정을 취소합니다.')
                    break
                
                else :
                    print('올바른 번호를 입력해주세요.')



#--------------------------------------------------------------------------------------#

cnt = len(students)+1 # 학번
while True:
    choice = stu_first_screen()
    
    # 1. 학생성적입력 프로그램
    if choice == 1:
        stu_input(cnt)
    
    # 2. 학생성적출력 프로그램
    elif choice == 2 :
        stu_print_all()

    # 3. 학생검색 프로그램
    elif choice == 3 :
       stu_print_search()
                       
    # 4. 학생수정 프로그램 
    elif choice == 4:
        stu_update_list()
    
    # 등수 처리
    elif choice == 5:     
        stu_rank()
                    
    # 학생 삭제  
    elif choice == 6:
        while True:
            search = input('삭제하고자 하는 학생의 이름을 입력하세요(0.취소) >> ')
            chk = 0
            if search == '0':
                print('학생삭제을 취소합니다.')
                break
            
            for i in students:
                if search == i['name']:
                    break
                chk += 1    
                    
            print('찾고자 하는 학생의 위치 :',chk)
            
            if chk >= len(students):
                print('찾고자 하는 학생이 없습니다.')
            else :
                print(f'{search}학생의 정보가 있습니다')
                s_input = input(f'{search}학생 성적을 삭제하시겠습니까?(0. 취소, 1. 삭제)')
                #삭제
                if s_input != '1':
                    print('f{search}학생의 삭제를 취소했습니다.')
                    break
                else : 
                    del students[chk]
                    print(f'{search}학생의 성적이 삭제되었습니다.')
                    
            print(students)
            
    # 0. 프로그램 종료
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break # 반복문 종료
