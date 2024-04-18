students = []

with open('stu.txt','r',encoding='utf8') as f:
    while True:
        txt = f.readline().strip()
        if txt == '': break
        
        s_list = txt.split(',')
        # print(s_list)

        student = {'stuNo':int(s_list[0]),'name':s_list[1],'kor':int(s_list[2]),'eng':int(s_list[3]),
                   'math':int(s_list[4]),'total':int(s_list[5]),'avg':float(s_list[6]),'rank':int(s_list[7])}
        
        students.append(student)
