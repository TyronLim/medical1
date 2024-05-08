# # stu.txt 파일을 출력하시오.
# file = open('stu.txt','r',encoding='utf-8')

# read = file.read()
# print(read)

# file.close()

# stu.txt 파일을 리스트로 출력해서 하나하나 출력하시오.
# file = open('stu.txt','r',encoding='utf-8')
# stuNo,name,kor,eng,math,total,avg = file.readline().split(',')
# r_list = [0]*7
# r_list[0] = int(stuNo)
# r_list[1] = name
# r_list[2] = int(kor)
# r_list[3] = int(eng)
# r_list[4] = int(math)
# r_list[5] = int(total)
# r_list[6] = float(avg)

# for i in r_list:
#     print(i,end =' ')
    
# file.close()


# stu.txt 파일을 리스트로 출력해서 하나하나 출력하시오.2번째
# file = open('stu.txt','r',encoding='utf-8')
# r_list = file.readline().split(',')
# r_list[0] = int(r_list[0])
# r_list[1] = r_list[1]
# r_list[2] = int(r_list[2])  # 국어
# r_list[3] = int(r_list[3])
# r_list[4] = int(r_list[4])
# r_list[5] = int(r_list[5])
# r_list[6] = float(r_list[6])
# print(r_list)
# file.close()






# 파일 읽어오기

# file = open('이번엔쉽게.txt','r',encoding='utf-8')
# while True:
#     txt = file.readline()       # 1줄만 읽어오기
#     if txt == '':
#         break
#     print(txt,end='')

# file.close()


# 파일 저장
# file = open('이번엔쉽게.txt','w',encoding='utf-8')

# file.write('안녕하세요\n')
# file.write('반갑습니다\n')
# file.write('파이썬수업입니다.\n')

# file.close()
# print('파일이 저장되었습니다.')