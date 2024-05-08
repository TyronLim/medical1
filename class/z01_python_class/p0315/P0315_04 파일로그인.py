# 로그인
f = open('mem.txt','r',encoding='utf8')


tmp = 0
while True:
    if tmp == 1:
        break
    print('-'*50)
    print('\t\t[ 로그인 ]')
    print('-'*50)
    print('로그인이 필요한 서비스입니다.')
    c_id = input('ID를 입력하세요 >> ')
    c_pw = input('PASSWORD를 입력하세요 (0. 종료)>> ')
    
    if c_pw == '0': break
    
    # mem.txt 파일을 불러와서 아이디, 패스워드를 비교
    success_flag = 0
    while True:
        m = f.readline()
        if m == '': break
        member = m.strip().split(',')
        
        if c_id == member[0] and c_pw == member[1]:
            success_flag = 1

    f.close()
    
    if success_flag == 0:
        print('ID나 PASSWORD가 일치하지 않습니다. 다시 입력해주세요.')
        print()
        
    else :
        print('로그인 되었습니다.')
        print()
            
        while True:
            print('-'*50)
            print('[ 학생성적 프로그램 ]')
            print('-'*50)
            print('1. 학생성적데이터 읽어오기')
            print('2. 학생성적입력')
            print('3. 학생성적출력')
            print('0. 프로그램 종료')
            print('-'*50)
            choice = input('원하는 번호를 입력하세요 >> ')
            # if not choice.isdigit:
            #     print('숫자를 입력하세요.')
            # choice == int(choice)
            if choice == '1':
                pass
            
            elif choice == '0':
                tmp = 1
                break
            
                    
        
        
print('프로그램을 종료합니다.뿅')
        
        
        
        
        