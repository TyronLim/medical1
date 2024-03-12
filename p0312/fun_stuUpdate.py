# 성적점수부분 함수
def score_update(s_title,stu,choice):
    print(f' [{s_title[choice+1]}성적수정] ')
    print(f'현재 {s_title[choice+1]}점수 :',stu[choice+1])
    print('-'*30)
    stu[choice+1] = int(input('수정할 점수를 입력하세요 >> '))
    print(f'수정된 {s_title[choice+1]}점수 :',stu[choice+1])
    stu[5] = stu[2]+stu[3]+stu[4]                   # 총점 수정
    stu[6] = float('{:.2f}'.format(stu[5]/3))       # 평균 수정
    print(f'{s_title[choice+1]}점수가 수정되었습니다.')


# 학생성적수정함수
def stu_update(s_title,stu,choice):
    print('[ 학생성적수정 ]')
    print('1. 국어  2.영어  3.수학')
    choice = int(input('원하는 번호를 입력하세요 >> '))
    
    if choice == 1:
        score_update(s_title,stu,choice)
        
    elif choice == 2:
        score_update(s_title,stu,choice)
        
    elif choice == 3:
        score_update(s_title,stu,choice)