
tmp = 0
while True:
    if tmp == 1:
        break
    print('-'*50)
    print('[ 회원정보 ]')
    print('-'*50)
    print('1. 회원가입')
    print('2. 로그인')
    print('3. 회원정보수정')
    print('0. 종료')
    print('-'*50)

    choice = int(input('원하는 번호를 입력하세요 >> '))
    

    if choice == 1:
        print('-'*50)
        print('\t\t[ 회원가입 ]')
        print('-'*50)
        print('회원 정보를 입력해주세요.')
        print()
        c_id = input('아이디를 입력하세요 >> ')
        c_pw = input('패스워드를 입력하세요 >> ')
    
        f = open('mem.txt','a',encoding ='utf8')
        m = f.write(f'{c_id},{c_pw}\n')
        
        f.close()
        print('회원가입이 완료되었습니다')
        
    elif choice == 2:     
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


    
    elif choice == 3:
        print('[ 회원정보 수정 ]')
        # 파일에 있는 모든 정보를 list에 우선 저장
        mem = []
        f = open('mem.txt','r',encoding='utf')
        
        while True:
            txt = f.readline()
            if txt == '': break
            t_list = txt.strip().split(',')
            mem.append([t_list[0],t_list[1]])
        
        f.close()
        
        search = input('수정할 ID를 입력하세요 >> ')
        
        cnt = 0
        for m in mem:
            if search == m[0]:
                break
            cnt += 1
            
        if cnt == len(mem):    
            print('찾고자 하는 ID가 없습니다. 다시 입력하세요.')
        
        else :
            print('패스워드 수정')
            pw_input = input('수정할 패스워드를 입력하세요.')        
            mem[cnt][1] = pw_input
            
            f = open('mem.txt','w',encoding='utf')

            for m in mem:
                txt = f.write(f'{m[0]},{m[1]}\n')
            f.close()
        
    elif choice == 0:
        break