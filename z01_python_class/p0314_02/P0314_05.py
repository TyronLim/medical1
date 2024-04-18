import os

while True:
    print('[ 윈도우 탐색기 ]')
    print('-'*50)
    print('1. 폴더 내 파일 확인')
    print('2. 파일 불러오기')
    print('3. 파일 저장')
    print('-'*50)
    choice = input('원하는 번호를 입력하세요')
    if not choice.isdigit:
        print('올바른 번호를 입력하세요.')
    choice = int(choice)        
    
    if choice == 1:
        print('[ 폴더 내 파일 ]')
        # print(os.listdir())
        a = os.listdir()
        for i in a:
            if i.find('.') != -1:
                print(i)
        
        # for i in range(len(a)):
        #     # print(a[i])
        #     if '.' in a[i]:
        #         print(a[i])
            
            
    elif choice == 2:
        print('[ 파일 불러오기 ]')
        a = os.listdir()
        for i in a:
            if i.endswith('.txt'):
                print(i)
        print('-'*50)
        search = input('파일명을 입력하세요. >>')
        f = open(f'{search}.txt','r',encoding='utf-8')
        while True:
            txt = f.readline()
            print(txt,end='')        
            if txt == '':
                break
        
        f.close()


    elif choice == 3:
        print('[ 파일 저장 ]')
        print('1. 기존파일에 저장하기')
        print('2. 새로운파일에 저장하기')
        choice = int(input('번호를 입력하세요 >> '))
        if choice == 1:
        
            a = os.listdir()
            for i in a:
                if i.endswith('.txt'):
                    print(i)
            print('-'*50)
            search = input('파일명을 입력하세요. >>')
            
            f = open(f'{search}.txt','a',encoding='utf-8')  # 파일 열기
            
            print('[ 아래에 글을 입력하세요 ]')
            while True:                                     # 파일 쓰기
                txt_input = input('')
                f.write(txt_input)
                
                if txt_input == '-1':
                    break
        
            print('파일에 텍스트를 추가저장했습니다.')
            f.close()
        
        elif choice == 2:
            a = os.listdir()
            for i in a:
                if i.endswith('.txt'):
                    print(i)
            print('-'*50)
            search = input('파일명을 입력하세요. >>')
            
            f = open(f'{search}.txt','w',encoding='utf-8')  # 파일 열기
            
            print('[ 아래에 글을 입력하세요 ]')
            while True:                                     # 파일 쓰기
                txt_input = input('')
                f.write(txt_input+'\n')
                
                if txt_input == '-1': break
                
            print('파일에 텍스트를 추가저장했습니다.')
            f.close()
                
    elif choice == 0:
        print('종료')
        break