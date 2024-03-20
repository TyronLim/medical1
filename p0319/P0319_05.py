name = ['홍길동','유관순','이순신','김구','강감찬','홍길순','홍길자']

## 정확한 이름으로 찾는 방법 ##
# while True:
#     cnt = 0
#     search = input('이름을 입력하세요 >> ')
#     for n in name:
#         if search == n:
#             print('학생의 위치 : ',cnt)
#             break
#         cnt += 1
            
#     if cnt == len(name):
#         print('학생이 없습니다.')
        

## 검색어가 포함이 되어 있어도 검색하는 방법
while True:
    cnt = 0
    search = input('이름을 입력하세요 >> ')
    l= []
    for n in name:
        if search in n:
        # if n.find(search) != -1:          >> 검색어가 포함 되어 있는지 확인. 포함 안 되면 -1, 포함 되면 개수
            # print('검색된 학생 : {}'.format(name[cnt]))
            l.append(n)
        cnt += 1
        
    if len(l) == 0:
        print('검색 결과가 없습니다.')
    
    else:
        print(f'{search}(으)로 검색된 결과')
        for i in l:
            print(i,end = ' ')
        print()
        print()
