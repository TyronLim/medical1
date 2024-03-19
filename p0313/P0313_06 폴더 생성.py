import os

print('현재 운영체제 :',os.name) # 윈도우 nt
print('현재 폴더위치 :',os.getcwd()) # 현재 폴더
print('현재 폴더 내 파일 표시 :',os.listdir()) # 폴더 내 모든 파일 출력

# 폴더 생성
# os.mkdir('빛바랜새부리')

# 폴더 삭제
# os.rmdir('빛바랜새부리')

# 파일 생성
with open ('students.txt','w') as f:
    f.write("1, '홍길동', 100, 100, 100, 300, 100.00, 0")
    
str1 = "1, '홍길동', 100, 100, 100, 300, 100.00, 0"
s_list = str1.split(',')

# for i in s_list:
#     print(i)