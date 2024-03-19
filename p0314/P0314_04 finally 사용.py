# 파일 1개 저장

# file open
file = open('memo.txt','w',encoding='utf8')
try:
    # file write
    file.write('안녕하세요.\n')
    file.write('안녕하세요.\n')
    file.write('안녕하세요.\n')
    print(1/0)
    file.write('안녕하세요.\n')
except Exception as e:      # Exception = 출력하면 예외(오류) 설명.
    print('저장시 에러가 났습니다.')
    print(e)
    
finally:    ## 오류가 나든 안 나든 파일을 닫고 싶을 때 사용.
    file.close()    # 파일닫기


