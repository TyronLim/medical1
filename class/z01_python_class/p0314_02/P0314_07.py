# str.txt 파일의 내용을 모두 출력하시오.

# str.txt 파일 내용을 읽어와서 str1에 추가해보세요.

f = open('str.txt','r',encoding='utf-8')

while True:
    txt = f.readline()
    if txt == '':
        break
    print(txt,end='')
    ff = open('str1.txt','a',encoding='utf-8')
    txt2 = ff.write(txt)

f.close()
ff.close()

# print('-'*50)

# fff = open('str1.txt','r',encoding='utf-8')
# while True:
#     txt3 = fff.readline()
#     if txt3 == '': break

#     print(txt3)

# ffff= open('str1.txt','r',encoding='utf-8')
# while True:
#     txt4 = ffff.readline()
#     if txt4 == '': break
#     print(txt4)
    
# ffff.close()

    
# fffff = open('str1.txt','r',encoding='utf-8')
# f_list = fffff.readlines()
# print(f_list)

# fffff.close()

# import os 

# if os.path.exists('str1.txt'):
#     with open('str1.txt','r',encoding='utf-8') as f6:
#         while True:
#             txt6 = f6.readline()
#             if txt6 == '': break
#             # print(txt6)


            
#             f6.write('안녕하세요. 반갑습니다.')
#             print(txt6)
    


