import os

# print('현재 폴더 내 파일 표시 :',os.listdir()) # 폴더 내 모든 파일 출력

######폴더가 존재하는 지 확인#######
# if not os.path.exists('상고머리독수리'):
#     os.mkdir('상고머리독수리')  
# else:
#     print('폴더가 이미 존재합니다. 삭제합니다.')
#     os.rmdir('상고머리독수리')


# 파일 쓰기 방법1
# f = open ('students.txt','w')
# f.write("1, '홍길동', 100, 100, 100, 300, 100.00, 0")
# f.write("2, '유관순', 100, 100, 100, 300, 100.00, 0")
# f.close()           # 파일 닫기 

# # 파일 생성 방법2 - with를 사용하면 f.close() 사용하지 않아도 됨.
# with open('students.txt','w'):
#     f.write("1, '홍길동', 100, 100, 100, 300, 100.00, 0")
    
# 파일읽어오기
# out_f = open('students.txt','r')
# t_list = []
# while True:
#     txt = out_f.readline()  # 1줄씩 읽어오기
#     # print(type(txt))
#     if txt == '':
#         break
#     print(txt,end='')
#     t_list.append(txt)
    
# print()
# print(t_list)

# 파일 삭제

os.remove('students.txt')


    
    