stu = [
    ['홍길동',100],
    ['유관순',98],
    ['이순신',95],
    ['김구',50],
    ['강감찬',99],
    ['김유신',90],
    ['홍길순',80],
    ['홍길자',70]
    ]

# 이름으로 검색, 홍이 들어가는 사람을 모두 검색해서 출력하시오.
# 이름으로 검색, 신이 들어가는 사람을 모두 검색해서 출력하시오.


while True:
    print('[ 학생성적 검색 ]')
    print('1. 이름으로 검색')
    print('2. 점수 검색')
    choice = input('검색할 항목을 선택하세요 >> ')
    if choice.isdigit():
        choice = int(choice)
    
    if choice == 1:    
        s_list = []
        search = input('검색어를 입력하세요 >> ')
        cnt = 0
        for i in stu:
            # if i[0].find(search) != -1:
            if search in i[0]:
                s_list.append(i[0])
            cnt += 1
            
        if len(s_list) == 0:
            print('학생이 없습니다.')
        
        else : 
            print("-"*50)
            print('{}(으)로 검색하신 결과'.format(search))
            for i in s_list:
                print(i,end = ' ')
            print()
            print("-"*50)
    
    elif choice == 2:
        l_list = []
        tmp = 0
        score = input('몇 점 이상을 검색하시겠습니까 >> ')
        if score.isdigit():
            score = int(score)
            
        for i in stu:
            if score <= i[1]:
                l_list.append(i[0])
            tmp += 1
        
        if len(l_list) == 0:
            print('-'*50)
            print('{}점 이상의 학생이 없습니다.'.format(score))
            print('-'*50)

        else:
            print('-'*50)
            print('{}점 이상 검색결과'.format(score))
            print('-'*50)
            for i in l_list:
                print(i,end = ' ')
            print()             
            print('-'*50)
            
            
    
    
    
    
    