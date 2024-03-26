# medical_1.csv 파일을 읽어와서 출력하시오.

f = open('medical_1.csv','r',encoding='UTF-8')

cnt = 0
# s_list = []
while True:
    content = f.readline()
    if cnt == 0 :
        cnt+=1
        continue
    if content == '': break
    s_list = content.split(',')
    
    
    print(s_list)
f.close()
# del s_list[len(s_list)-1]

# print(s_list)
# sum = 0
# for i in s_list:
#     sum += int(i[1])
#     print(i[1])

# print(sum)



