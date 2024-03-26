import fun_stuUpdate


#------------------------------------------------------------------------

stu = [1,'홍길동',100,100,100,300,100.0,1]
s_title = ['번호','이름','국어','영어','수학','총점','평균','등수']

while True:
    print('-'*50)
    print('학생데이터:',stu)
    print('3.학생성적수정')
    print('0.종료')
    choice = int(input('원하는 번호를 입력하세요 >> '))

    if choice == 3: # 학생성적수정
        fun_stuUpdate.stu_update(s_title,stu,choice)
        
    else :
        print('[ 프로그램종료 ]')
        break