import random

words = [
        {},
        
        {'airplane' : '비행기', 'appel' : '사과', 'bakery' : '빵집',  
        'banana' : '바나나', 'bank' : '은행', 'bean' : '콩',  
        'bicycle' : '자전거', 'boat' : '보트',  'bowl' : '그릇', 'bus' : '버스'},
        
        {'bake':'굽다', 'blow':'불다', 'check':'확인하다',
        'chew':'씹다', 'close':'닫다', 'dance':'춤추다',
        'walk':'걷다', 'work':'일하다', 'drink':'마시다', 'eat':'먹다'},
        
        {"agile":"민첩한", "ambitious":"야망있는", "awkward":"서투른",
        "bountiful":"너그러운", "clumsy":"어설픈", "courteous":"공손한",
        "exrovert":"외향적인", "genial":"상냥한", "introvert":"내향적인", "picky":"까다로운"}
        ]

w_noun = {
        'airplane' : '비행기',
        'appel' : '사과',  
        'bakery' : '빵집',  
        'banana' : '바나나',  
        'bank' : '은행',  
        'bean' : '콩',  
        'bicycle' : '자전거',  
        'boat' : '보트',  
        'bowl' : '그릇',  
        'bus' : '버스' 
        }

w_verb = {
        'bake':'굽다',
        'blow':'불다',
        'check':'확인하다',
        'chew':'씹다',
        'close':'닫다',
        'dance':'춤추다',
        'walk':'걷다',
        'work':'일하다',
        'drink':'마시다',
        'eat':'먹다'
        }

w_ad = {
        "agile":"민첩한",
        "ambitious":"야망있는",
        "awkward":"서투른",
        "bountiful":"너그러운",
        "clumsy":"어설픈",
        "courteous":"공손한",
        "exrovert":"외향적인",
        "genial":"상냥한",
        "introvert":"내향적인",
        "picky":"까다로운"
        }

w_title = ['','명사','동사','형용사']


# 함수 선언
def w_quiz(choice):
    print('{}를 선택하셨습니다.'.format(w_title[choice]))
    chk = input('{}퀴즈가 나갑니다. 준비되셨나요?(1.실행 / 0.취소)'.format(w_title[choice]))
    if chk == '1':         
        list_w = list(words[choice].keys())
        list_w_random = random.sample(list_w,5) 
        
        # key = 영어, value = 한글
        # print(w_noun.keys()) = 전체 key
        # print(w_noun.values()) = 전체 value
        print('시~작!')
        right = 0
        for key in list_w_random:
            # print(key,':',w_noun[key]) = 둘 다 출력
            answer = input(f'{key}의 뜻 : ')  # 영어를 보여주고 뜻을 물어보는 형식
            if answer == words[choice][key]:
                print('[딩동댕!!! 정답입니다.]')
                right += 1
            else:
                print(f'[땡!!! 틀렸습니다. 정답은 {words[choice][key]}입니다]')                
        print('[[[[[맞춘 개수는 {}개, 틀린 개수는 {}개입니다.]]]]]'.format(right, len(list_w_random)-right))
    
    else :
        print('퀴즈를 취소하셨습니다. 메뉴로 돌아갑니다.')    


while True:
    print('[영단어 맞추기 프로그램]')
    print('-'*50)
    print('1. 명사')
    print('2. 동사')
    print('3. 형용사')
    print('0. 종료')
    print('-'*50)
    choice = int(input('원하는 번호를 입력하세요 >> '))      # 정수형으로 받음
    if choice == 1:
        w_quiz(choice)
            
    elif choice == 2:
        w_quiz(choice)
        
    elif choice == 3:
        w_quiz(choice)

    else :
        print('프로그램을 종료합니다.')
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    