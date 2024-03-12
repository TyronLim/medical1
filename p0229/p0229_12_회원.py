
member = []
# 이름을 입력받아서 [1,홍길동] [2,유관순] [3,이순신]
i = 0    
while True:
    print('-'*25)
    print('1. 입력')
    print('2. 출력')
    print('3. 검색출력')
    print('4. 검색삭제')
    print('5. 수정')
    print('0. 종료')
    ch = input('원하는 번호를 선택하세요>> ')
    print('-'*25)
    if ch.isdigit():
        ch = int(ch)
   

    if ch == 1:
        print('입력')
        name = input('이름을 입력해주세요 >> ')
        i += 1
        m = [i, name]
        member.append(m)
        
    elif ch == 2:
        print('출력')
        print('번호\t이름')
        for j in range(len(member)):
            print('{}\t{}'.format(member[j][0],member[j][1]))
        
        # for j in range(len(member)):
        #     for k in range(len(member[j])):
        #         print(member[j][k], end = ' ')
        #         print()
    
    elif ch == 3:
        search = input('검색 출력할 학생의 이름을 입력해주세요 >>')
        print('번호\t이름')
        for k, stu in enumerate(member):
            if search in stu:
                print('{}\t{}'.format(member[k][0],member[k][1]))
    
    elif ch == 4:
        search2 = input('삭제할 학생의 이름을 입력해주세요 >> ')
        print('번호\t이름')
        for n, m in enumerate(member):
            if search2 in m:
                del(member[n])
                print('{}\t{}'.format(n,search2))
                print('학생이 삭제되었습니다.')
    
    elif ch == 5:
        search3 = input('수정할 학생 이름을 입력해주세요 >> ')
        for i,m in enumerate(member):
            if search3 in m:
                print(search3,'님을 선택하셨습니다.')
                ch_num = int(input('1 = 번호 수정  , 2 = 이름 수정 >> '))
                if ch_num == 1:
                    print(search3,'님의 번호 수정을 선택하셨습니다.')
                    print(search3,'님의 번호는 {}번입니다.'.format(member[i][0]))
                    ch_mem_num = int(input('수정할 번호를 입력해주세요 >> '))
                    member[i][0] = ch_mem_num
                    print(search3,'님의 번호가 {}에서 {}로 수정되었습니다.'.format(member[i][0],ch_mem_num))
                elif ch_num == 2:
                    print(search3,'님의 이름 수정을 선택하셨습니다.')
                    print(search3,'님의 이름은 {}번입니다.'.format(member[i][1]))
                    ch_mem_name = int(input('수정할 이름을 입력해주세요 >> '))
                    member[i][1] = ch_mem_name
                    print(search3,'님의 번호가 {}에서 {}로 수정되었습니다.'.format(member[i][0],ch_mem_num))
                
    elif ch == 0:
        print('종료')
        break
    
    else :
        print('숫자를 다시입력해주세요')
    
