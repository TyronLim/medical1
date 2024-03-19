####### 파일 읽어오기

# 1. 파일 열기
# read() : 모든 문자열을 가져옴.
# readline() : 한 줄씩 가져옴
# readlines() : 한 줄씩 모든 문장을 가져옴 리스트로.
# 3. 파일 닫기
import os

if os.path.exists('이번엔쉽게.txt'):
    with open('이번엔쉽게.txt','r',encoding='utf-8') as f:## 별칭(변수명)을 뒤에 씀.    ## close 생략 가능
        txt_list = f.readlines()

        for txt in txt_list:
            print(txt,end='')
        print()
else :
    print('파일이 없습니다.')


# readlines   # 1줄씩 리스트 타입으로 가져오기
# f = open('이번엔쉽게.txt','r',encoding='utf8')
# # 1줄씩 리스트타입으로 저장
# txt_list = f.readlines()
# print(txt_list[0])
# f.close()                           >> 파일 종료를 반드시 해야 함


# f = open('이번엔쉽게.txt','r',encoding='utf8')
# while True:
#     if txt == '':
#         break
#     print(txt,end = ' ')
# f.close()