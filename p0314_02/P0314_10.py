# f = open('k001.csv','r',encoding='utf8')

# cnt = 0
# sum = 0
# c_list = []
# while True:
#     content = f.readline()
#     if cnt == 0:
#         cnt +=1
#         continue
#     if content == '': break
#     c_list.append(content.split(','))

# f.close()
# # print(c_list)

# for i in c_list:
#     sum += int(i[4])

# print(sum)



ff = open('k001.csv','r',encoding = 'utf8')
cnt = 0
sum = 0
while True:
    f2 = ff.readline()
    if cnt == 0:
        cnt +=1
        continue
    
    if f2 == '': break
    
    f_list=f2.split(',')
    
    sum += int(f_list[4])

print(sum)