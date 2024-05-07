students=[]

with open('./d0507/stu_score1.csv','r',encoding='utf8') as f:
    while True:
        txt = f.readline()
        if txt == '':break
        stu = txt.split(',')
        s_li=[stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7],stu[8]]
        
        students.append(s_li)

print(students)        

# for i in range(students):
#     for j in range(i):
#         print(j,end=' ')
#     print()